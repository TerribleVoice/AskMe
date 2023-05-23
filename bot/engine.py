import sys

sys.path.append('C:\\Users\\Gorob\\Desktop\\bot\\keyboards')
sys.path.append('C:\\Users\\Gorob\\Desktop\\bot\\database')

from aiogram import Bot, Dispatcher, executor, types
from database import db
from keyboard import keyboard_start, keyboard_auth, keyboard_search_user_subscribe, keyboard_search_user, keyboard_subs
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import configparser

config = configparser.ConfigParser()
config.read('C:\\Users\\Gorob\\Desktop\\bot\\settings\\config.ini')

bot = Bot(token=config.get('BOT', 'TOKEN_BOT'))
dp = Dispatcher(bot, storage=MemoryStorage())

# Авторизация аккаунта пользователя
class Auth(StatesGroup):
    login = State()
    password = State()
    
# Поиск пользователя
class SearchUser(StatesGroup):
    nickname = State()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    telegram_id = message.chat.id
    check_conn = db.check_user_active(telegram_id=telegram_id)
    if check_conn == []:
        await message.answer("""
Здравствуйте, вам необходимо авторизоваться в ваш аккаунт!                             
""", reply_markup=keyboard_start)
    else:
        await message.answer("""
С возвращением!
""", reply_markup=keyboard_auth)
    
@dp.callback_query_handler(text='auth')
async def auth_command(call: types.CallbackQuery):
    await call.message.answer("""
Для авторизации вам необходимо ввести логин и пароль. Для начала введите логин!                              
""")
    await Auth.login.set()
    
@dp.message_handler(state=Auth.login)
async def auth_login(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['login'] = message.text
        await message.answer(text="👇Теперь введите пароль!")
        await Auth.password.set()
        
    except Exception as ex:
        await Auth.login.set()
        await message.answer(f"""
Введите логин повторно!
""")
        
@dp.message_handler(state=Auth.password)
async def auth_password(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['password'] = message.text
        auth = db.check_auth(login=data['login'], password=data['password'])
        if auth == []:
            await message.answer("""
Логин или пароль введены неверно!
""")
            await state.finish()
        else:
            db.add_user_active(telegram_id=message.chat.id, user_id=auth[0][0])
            await message.answer("""
Вы успешно авторизовались!
""", reply_markup=keyboard_auth)
            await state.finish()
                
    except Exception as ex:
        await Auth.password.set()
        await message.answer(f"""
Введите пароль повторно!
""")
    
@dp.callback_query_handler(text='find_user')
async def find_user_command(call: types.CallbackQuery):
    await call.message.answer("Пожалуйста, введите никнейм пользователя!")
    await SearchUser.nickname.set()
        
@dp.message_handler(state=SearchUser.nickname)
async def find_user_nickname(message: types.Message, state: FSMContext):    
    try:
        async with state.proxy() as data:
            data['nickname'] = message.text
        search_user = db.seacrh_user(nickname=data['nickname'])
        
        # Если не нашел - то пользователь не найден
        if search_user == []:
            anybody = db.search_many_user(nickname=data['nickname'])
            if anybody == []:
                await message.answer("Данный пользователь не найден!")
            else:    
                await message.answer("Данный пользователь не найден!\nНо мы нашли вам похожих пользователей, возможно вы искали их!\n")
        else:
            user_id = db.check_user_active(telegram_id=message.chat.id)[0][0]
            author_id = db.get_author_id(nickname=data['nickname'])[0][0]
            subscribe_user = db.check_user_subscription(user_id = user_id, subscription_id=author_id)
            if subscribe_user == []:   
                await message.answer("Данный пользователь найден!", reply_markup=keyboard_search_user)
            else:
                await message.answer("Данный пользователь найден!", reply_markup=keyboard_search_user_subscribe)
        
        await state.finish()
        
    except Exception as ex:
        await SearchUser.nickname.set()
        await message.answer(f"""
Введите никнейм пользователя повторно!
""")
        
@dp.callback_query_handler(text='subscribe_user')
async def subscribe_user_command(call: types.CallbackQuery):
    pass

@dp.callback_query_handler(text='list_subs')
async def list_subs_command(call: types.CallbackQuery):
    user_id = db.check_user_active(telegram_id=call.message.chat.id)[0][0]
    all_subs = db.get_all_subscriptions(user_id = user_id)
    if all_subs == []:
        await call.message.answer("У вас нет подписок!")
    else:
        for sub in all_subs:
            sub_id = all_subs[0][2]
            sub_info = db.get_info_subs(sub_id = sub_id)[0]
            await call.message.answer(f"""
Имя: {sub_info[3]}\n
Описание: {sub_info[4]}                                      
""", reply_markup=keyboard_subs)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)