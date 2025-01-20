from aiogram.types import Message
from aiogram.filters import BaseFilter

import database.queries as db


class HasPremissonsFilter(BaseFilter):
    async def __call__(self, message: Message):
        user = await db.get_user(message.from_user.id)
        if user and user.key:
            return True
        return False
