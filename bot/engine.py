import sys

sys.path.append('C:\\Users\\Gorob\\Desktop\\bot\\keyboards')
sys.path.append('C:\\Users\\Gorob\\Desktop\\bot\\database')

from aiogram import Bot, Dispatcher, executor, types
from database import db
from keyboard import keyboard_start
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import configparser

config = configparser.ConfigParser()
config.read('C:\\Users\\Gorob\\Desktop\\bot\\settings\\config.ini')

bot = Bot(token=config.get('BOT', 'TOKEN_BOT'))
dp = Dispatcher(bot, storage=MemoryStorage())

class Auth(StatesGroup):
    login = State()
    password = State()

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
Вы в аккаунте уже активированы!
""")
    
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
""")
            await state.finish()
            
    except Exception as ex:
        await Auth.password.set()
        await message.answer(f"""
Введите пароль повторно!
""")
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)