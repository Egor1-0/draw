from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

import keyboards.user as user_kb
import database.queries as db
from filters import HasPremissonsFilter

router = Router()

router.message.filter(~HasPremissonsFilter())


@router.message(CommandStart())
async def start(message: Message):
    """обработка старта для юзеров которые не ввели ключ.
    для доступа к функционалу необходимо получить ключ от администрации"""
    await db.add_user(tg_id=message.from_user.id)
    await message.answer('Введите ключ, который вам дал админ')


@router.message(F.text)
async def get_key(message: Message):
    """ввод ключа и сохранение его в бд"""
    key = await db.get_key(key=message.text)
    if not key or key.user:
        await message.answer('Неправильный ключ')
        return
    user = await db.get_user(message.from_user.id)
    await message.answer('Вам доступен функционал', reply_markup=user_kb.start_kb)
    await db.add_key(user_id=user.id, key=key.value)
