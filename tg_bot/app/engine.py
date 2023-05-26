import sys
import uuid
import asyncio

sys.path.extend(['./keyboards', './database'])

from aiogram import Bot, Dispatcher, executor, types
from database import db
from keyboard import keyboard_start, keyboard_auth, keyboard_search_user_subscribe, keyboard_search_user, keyboard_subs, keyboard_login, keyboard_password, \
                     keyboard_auth_again, keyboard_register_login, keyboard_register_email, keyboard_email_wrong, keyboard_register_password, \
                     keyboard_login_register, keyboard_subscribe_back, keyboard_nickname_again
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import configparser

config = configparser.ConfigParser()
config.read('./settings/config.ini')

bot = Bot(token=config.get('BOT', 'TOKEN_BOT'))
dp = Dispatcher(bot, storage=MemoryStorage())

# Регистрация аккаунта пользователя
class Register(StatesGroup):
    login = State()
    email = State()
    password = State()

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
Здравствуйте, вам необходимо войти в свой аккаунт или пройти регистрацию в Сервисе AskeMe!                        
""", reply_markup=keyboard_start)
    else:
        await message.answer("""
С возвращением!
""", reply_markup=keyboard_auth)
        
@dp.callback_query_handler(text='exit_nickname')
async def exit_nickname_command(call: types.CallbackQuery):
    await call.message.answer("""
Выберите интересующее вас действие!
""", reply_markup=keyboard_auth)
    
@dp.callback_query_handler(text='subscribe_back')
async def keyboard_subscribe_back_command(call: types.CallbackQuery):
    await call.message.answer("""
Выберите интересующее вас действие!
""", reply_markup=keyboard_auth)
    
@dp.callback_query_handler(text='auth_email', state=Register.email)
async def auth_email_command(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer("""
Для входа вам необходимо ввести логин(или email) и пароль. Для начала введите логин(или email)!                           
""", reply_markup=keyboard_login)
    await Auth.login.set()
    
@dp.callback_query_handler(text='auth')
async def auth_command(call: types.CallbackQuery):
    await call.message.answer("""
Для входа вам необходимо ввести логин(или email) и пароль. Для начала введите логин(или email)!                           
""", reply_markup=keyboard_login)
    await Auth.login.set()
    
@dp.callback_query_handler(text='exit_login', state=Auth.login)
async def exit_login_command(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer("""
Здравствуйте, вам необходимо войти в свой аккаунт или пройти регистрацию в Сервисе AskeMe!                        
""", reply_markup=keyboard_start)

@dp.callback_query_handler(text='exit_login_register', state=Register.login)
async def exit_login_register_command(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer("""
Здравствуйте, вам необходимо войти в свой аккаунт или пройти регистрацию в Сервисе AskeMe!                        
""", reply_markup=keyboard_start)
                

@dp.message_handler(state=Auth.login)
async def auth_login(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['login'] = message.text
        await message.answer(text="👇Теперь введите пароль!", reply_markup=keyboard_password)
        await Auth.password.set()
        
    except Exception as ex:
        await Auth.login.set()
        await message.answer(f"""
Введите логин повторно!
""")
        
@dp.callback_query_handler(text='exit_password', state=Auth.password)
async def exit_password_command(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("""
Для входа вам необходимо ввести логин(или email) и пароль. Для начала введите логин(или email)!                           
""", reply_markup=keyboard_login)
    await Auth.login.set()
        
    

@dp.message_handler(state=Auth.password)
async def auth_password(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['password'] = message.text
        auth = db.check_auth(login=data['login'], password=data['password'])
        if auth == []:
            await message.answer("""
Логин или пароль введены неверно! Введите данные снова или зарегистрируйтесь.  
""", reply_markup=keyboard_auth_again)
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
        
@dp.callback_query_handler(text='auth_again')
async def auth_again_command(call: types.CallbackQuery):
    await message.answer("""
Здравствуйте, вам необходимо войти в свой аккаунт или пройти регистрацию в Сервисе AskeMe!                        
""", reply_markup=keyboard_start)
    
@dp.callback_query_handler(text='nick_again')
async def nick_again_command(call: types.CallbackQuery):
    await call.message.answer("Пожалуйста, введите никнейм пользователя!")
    await SearchUser.nickname.set()

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
            print(anybody)
            if anybody == []:
                await message.answer("Данного пользователя не удалось найти, просьба повторить попытку ввода.", reply_markup=keyboard_nickname_again)
            else:    
                await message.answer("Данный пользователь не найден!\nНо мы нашли вам похожих пользователей, возможно вы искали их!\n")
                for user in anybody:
                    user_id = db.check_user_active(telegram_id=message.chat.id)[0][0]
                    author_id = db.get_author_id(nickname=user[3])[0][0]
                    subscribe_user = db.check_user_subscription(user_id = user_id, subscription_id=author_id)
                    if subscribe_user == []:   
                        await message.answer(f"Имя: {user[3]}", reply_markup=keyboard_search_user)
                    else:
                        await message.answer(f"Имя: {user[3]}", reply_markup=keyboard_search_user_subscribe)
        else:
            user_id = db.check_user_active(telegram_id=message.chat.id)[0][0]
            author_id = db.get_author_id(nickname=data['nickname'])[0][0]
            subscribe_user = db.check_user_subscription(user_id = user_id, subscription_id=author_id)
            if subscribe_user == []:   
                await message.answer(f"Имя: {data['nickname']}\nДанный пользователь найден!", reply_markup=keyboard_search_user)
            else:
                await message.answer(f"Имя: {data['nickname']}\nДанный пользователь найден!", reply_markup=keyboard_search_user_subscribe)
        
        await state.finish()
        
    except Exception as ex:
        await message.answer(f"""
Введите никнейм пользователя повторно!
""")
        await SearchUser.nickname.set()

@dp.callback_query_handler(text='list_subs')
async def list_subs_command(call: types.CallbackQuery):
    user_id = db.check_user_active(telegram_id=call.message.chat.id)[0][0]
    all_subs = db.get_all_subscriptions(user_id = user_id)
    if all_subs == []:
        await call.message.answer("У вас нет подписок!")
    else:
        for sub in all_subs:
            sub_id = sub[2]
            sub_info = db.get_info_subs(sub_id = sub_id)[0]
            await call.message.answer(f"""
Имя: {sub_info[3]}\n
Описание: {sub_info[4]}                                      
""", reply_markup=keyboard_subs)
            
@dp.callback_query_handler(text='last_posts')
async def last_posts_command(call: types.CallbackQuery):
    info_message = call.message.text
    nickname = str(info_message.split("Имя: ")[1].split("\n")[0])
    author_id = db.get_author_id(nickname=nickname)[0][1]
    posts = db.get_posts_author(author_id=author_id)
    if posts == []:
        await call.message.answer(f"Пользователь {nickname} не имеет постов!")
    else:
        if len(posts) == 1:
            await call.message.answer(f"""
{posts[0][0]}
""")
        else:
            for post in posts:
                await call.message.answer(f"""
{post[0]}                                      
""")

@dp.callback_query_handler(text='view_posts')
async def view_posts_command(call: types.CallbackQuery):
    info_message = call.message.text
    nickname = str(info_message.split("Имя: ")[1].split("\n")[0])
    author_id = db.get_author_id(nickname=nickname)[0][1]
    posts = db.get_posts_author(author_id=author_id)
    if posts == []:
        await call.message.answer(f"Пользователь {nickname} не имеет постов!")
    else:
        if len(posts) == 1:
            await call.message.answer(f"""
{posts[0][0]}
""")
        else:
            for post in posts:
                await call.message.answer(f"""
{post[0]}                                      
""")
            
@dp.callback_query_handler(text='posts')
async def posts_command(call: types.CallbackQuery):
    user_id = db.check_user_active(telegram_id=call.message.chat.id)[0][0]
    posts = db.get_posts(user_id=user_id)
    if posts == []:
        await call.message.answer("Нет актуальных постов!")
    else:
        for post in posts:
            await call.message.answer(f"""
{post[0]}                                                                            
""")

# Регистрационный блок
@dp.callback_query_handler(text='register')
async def register_command(call: types.CallbackQuery):
    await call.message.answer("""
Для регистрации вам необходимо указать логин, email и пароль. Для начала введите логин!                              
""", reply_markup=keyboard_login_register)
    await Register.login.set()

@dp.message_handler(state=Register.login)
async def register_login_command(message: types.Message, state: FSMContext):    
    async with state.proxy() as data:
        data['login'] = message.text
    
    check_login = db.check_login(login=data['login'])
    if check_login == []:
        await message.answer("Далее введите ваш Email!", reply_markup=keyboard_register_email)
        await Register.email.set()
    else:
        await message.answer("Данный логин уже занят. Придумайте другой логин и введите его", reply_markup=keyboard_register_login)
        await Register.login.set()

@dp.callback_query_handler(text='exit_login_register', state=Register.login)
async def exit_login_register_command(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("""
Для регистрации вам необходимо указать логин, email и пароль. Для начала введите логин(или email)!                              
""", reply_markup=keyboard_login)
    await Register.login.set()

@dp.callback_query_handler(text='exit_email_register', state=Register.email)
async def exit_login_register_command(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("""
Для регистрации вам необходимо указать логин, email и пароль. Для начала введите логин(или email)!                              
""", reply_markup=keyboard_login)
    await Register.login.set()
    
@dp.message_handler(state=Register.email)
async def register_email_command(message: types.Message, state: FSMContext):    
    async with state.proxy() as data:
        data['email'] = message.text
    
    check_email = db.check_email(email=data['email'])
    if check_email == []:
        await message.answer("Придумайте и введите пароль, минимальная длина пароля 8 символов", reply_markup=keyboard_register_password)
        await Register.password.set()
    else:
        await message.answer("Данный email уже используется. Введите другой email или войдите  в свой аккаунт.", reply_markup=keyboard_email_wrong)
        await Register.email.set()
        
@dp.callback_query_handler(text='exit_password_register', state=Register.email)
async def exit_password_register_command(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Введите ваш Email!", reply_markup=keyboard_register_email)
    await Register.email.set()

@dp.message_handler(state=Register.password)
async def register_password_command(message: types.Message, state: FSMContext):    
    async with state.proxy() as data:
        data['password'] = message.text
    
    if len(data['password']) < 8:
        await message.answer("Пароль не соответствует условиям\nПридумайте и введите пароль, минимальная длина пароля 8 символов", reply_markup=keyboard_register_password)
        await Register.password.set()
    else:
        uuid_code = uuid.uuid1()
        db.create_account(uuid=uuid_code, login=data['login'], password=data['password'], email=data['email'])
        db.add_user_active(telegram_id=message.chat.id, user_id=uuid_code)
        await message.answer("Аккаунт успешно создан!\nПропишите /start!")
        await state.finish()
        
@dp.callback_query_handler(text='subscribe_user')
async def subscribe_user_command(call: types.CallbackQuery):
    uuid_code = uuid.uuid1()
    user_id = db.check_user_active(telegram_id=call.message.chat.id)[0][0]
    nickname = str(call.message.text.split("Имя: ")[1])
    author_id = db.get_author_id(nickname=nickname)[0][1]
    db.subscribe_user(uuid=uuid_code, user_id=user_id, subscription_id=author_id)
    await call.message.answer("Вы успешно подписались", reply_markup=keyboard_subscribe_back)

async def scheduled(wait_for):
     while True:
        posts = db.get_unactive_posts()
        for post in posts:
            sub_id = post[0]
            subscribers = db.get_all_subscribers(sub_id=sub_id)
            for subscriber in subscribers:
                user_id = subscriber[0]
                telegram_id = db.get_telegram_id_user(user_id=user_id)[0][0]
                nickname_author = db.get_name_author(author_id=sub_id)[0][0]
                await bot.send_message(chat_id=telegram_id, text=f"""У {nickname_author} вышел новый пост!\n\n{post[1]}""")
            db.add_post_active(id_post=post[2])
        
        await asyncio.sleep(wait_for)


async def on_startup(dp):
    asyncio.create_task(scheduled(2))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)