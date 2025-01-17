from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import keyboards.user as user_kb
import database.queries as db

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await db.add_user(tg_id=message.from_user.id)
    await message.answer('Приветственный текст', reply_markup=user_kb.start_kb)
