from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import keyboards.admin as admin_kb
import database.queries as db
from filters import IsAdmin

router = Router()

router.message.filter(IsAdmin())


@router.message(Command('admin'))
async def start(message: Message):
    await message.answer('Админская часть', reply_markup=admin_kb.main_admin)


@router.callback_query(F.data == 'create_key')
async def create_key(callback: CallbackQuery):
    key = await db.create_and_get_key()
    await callback.message.answer(key.value)
    await callback.answer()