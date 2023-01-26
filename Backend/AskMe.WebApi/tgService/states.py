from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    LOGIN = State()
    AMOUNT = State()
    MESSAGE = State()
    SENDER = State()
    DEFAULT = State()
