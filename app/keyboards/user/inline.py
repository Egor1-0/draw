from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.models.chat import Chat
from database.models.keyword import Keyword
from keyboards.user.factory import DeleteWordFactory, DeleteChatFactory

cancel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
], resize_keyboard=True)

def delete_keyword_kb(words: list[Keyword]):
    kb = InlineKeyboardBuilder()
    for word in words:
        kb.button(text=word.word, callback_data=DeleteWordFactory(word_id=word.id))

    kb.adjust(1)

    return kb.as_markup(resize_keyboard=True)

def delete_chat_kb(chats: list[Chat]):
    kb = InlineKeyboardBuilder()
    for chat in chats:
        kb.button(text=chat.name, callback_data=DeleteChatFactory(chat_id=chat.id))

    kb.adjust(1)

    return kb.as_markup(resize_keyboard=True)