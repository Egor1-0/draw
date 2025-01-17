from sys import prefix

from aiogram.filters.callback_data import CallbackData


class DeleteWordFactory(CallbackData, prefix='delete_word'):
    word_id: int