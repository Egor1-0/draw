from aiogram.filters.callback_data import CallbackData


class DeleteWordFactory(CallbackData, prefix='delete_word'):
    word_id: int


class DeleteChatFactory(CallbackData, prefix='delete_chat'):
    chat_id: int