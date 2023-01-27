import logging
import requests

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Users, Tokens

from utils import make_pg_url
from config import TG_TOKEN, DB_CONFIG
from states import States

logger = logging.getLogger(__name__)
bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class PayBot:
    session_factory = None

    @dp.message_handler(commands=['start'], state=[None, States.DEFAULT])
    async def start_message(message: types.Message):
        user = message.from_user
        await message.answer(
            f"Привет, {user.first_name} {user.last_name}! Я бот AskMe для приема донатов. Введи имя человека, которому ты хочешь задонатить.")
        await States.LOGIN.set()

    @dp.message_handler(state=States.LOGIN)
    async def login_message(message: types.Message, state: FSMContext):
        with session_factory() as session:
            q = session.query(Users).where(Users.login == message.text)
            user = session.execute(q).scalar()
            if not user:
                await message.answer(f"К сожалению, пользователя с именем {message.text} не существует, попробуйте еще раз")
                return
            elif not PayBot._check_bill(user.id, session):
                await message.answer(f"Пользователь с именем {message.text} еще не добавил себе функци доната. "
                                     f"Для выбора другого пользователя введите его имя.")
                return
        await state.update_data(receiver=str(user.id))
        await message.answer("Введите ваше имя, которое увидит получатель.")
        await States.SENDER.set()

    @dp.message_handler(state=States.SENDER)
    async def start_message(message: types.Message, state: FSMContext):
        await state.update_data(sender=message.text)
        await message.answer("Введите сообщение, которое вы хотите передать получателю.")
        await States.MESSAGE.set()

    @dp.message_handler(state=States.MESSAGE)
    async def start_message(message: types.Message, state: FSMContext):
        await state.update_data(comment=message.text)
        await message.answer("Введите сумму, которую вы хотите задонатить")
        await States.AMOUNT.set()

    @dp.message_handler(state=States.AMOUNT)
    async def start_message(message: types.Message, state: FSMContext):
        await state.update_data(amount=float(message.text))
        try:
            data = await state.get_data()
            response = requests.put('http://payment:4554/bill', json=dict(data))
            await message.answer(f"Ссылка для доната: {response.text} \n"
                                 f"Когда получатель ответит на донат, мы передадим вам его сообщение. \n"
                                 f"Если хотите отправить донат кому-то еще, то введите его имя")
        except Exception as ex:
            await message.answer(ex)
            #await message.answer("Произошла ошибка, попробуйте ввести имя получателя еще раз")
        await States.LOGIN.set()

    def _check_bill(user_id, session):
        q = session.query(Tokens).where(Tokens.author_id == user_id)
        token_obj = session.execute(q).scalar()
        return True if token_obj else False


if __name__ == '__main__':
    logger.info(f"Bot started")
    engine = create_engine(make_pg_url(**DB_CONFIG))
    session_factory = sessionmaker(bind=engine)
    PayBot.session_factory = session_factory
    executor.start_polling(dp, skip_updates=True)
