from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить ключевое слово'),
         KeyboardButton(text='Удалить ключевое слово')],
        [KeyboardButton(text='Добавить чат (канал)'),
         KeyboardButton(text='Удалить чат (канал)')],
        [KeyboardButton(text='Мои слова'),
         KeyboardButton(text='Мои чаты (каналы)')],
        [KeyboardButton(text='Поддержка')]
    ],
    resize_keyboard=True
)
