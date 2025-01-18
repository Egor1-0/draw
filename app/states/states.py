from aiogram.fsm.state import State, StatesGroup


class GetWord(StatesGroup):
    word = State()


class GetChat(StatesGroup):
    chat = State()