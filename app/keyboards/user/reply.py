from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить ключевое слово'),
         KeyboardButton(text='Удалить ключевое слово')],
        [KeyboardButton(text='Мои чаты'),
         KeyboardButton(text='Мои слова')],
        [KeyboardButton(text='Черный список')],
        [KeyboardButton(text='Поддержка')]
    ],
    resize_keyboard=True
)
