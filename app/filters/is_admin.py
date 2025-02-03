from aiogram.types import Message
from aiogram.filters import BaseFilter

import database.queries as db


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message):
        """проверка для доступа к админскому функционалу"""
        user = await db.get_user(message.from_user.id)
        if user and user.is_admin:
            return True
        return False
