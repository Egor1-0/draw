from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.models.keyword import Keyword
from keyboards.user.factory import DeleteWordFactory



cancel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
], resize_keyboard=True)

def delete_keyword_kb(words: list[Keyword]):
    kb = InlineKeyboardBuilder()
    for word in words:
        kb.button(text=word.word, callback_data=DeleteWordFactory(word_id=word.id))

    kb.adjust(1)

    return kb.as_markup(resize_keyboard=True)
