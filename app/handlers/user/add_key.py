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
    await message.answer('Введите ключ, который вам дал админ')


@router.message(F.text)
async def get_key(message: Message):
    key = await db.get_key(key=message.text)
    if not key:
        await message.answer('Неправильный ключ')
        return
    await message.answer('Вам доступен функционал', reply_markup=user_kb.start_kb)
    await db.add_key(tg_id=message.from_user.id, key=key.value)
