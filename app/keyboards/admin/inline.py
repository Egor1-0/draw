from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Создать ключ', callback_data='create_key')]
])