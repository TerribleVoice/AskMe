from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)