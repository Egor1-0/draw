from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.chat import Chat
from database.models.key import Key
from database.models.keyword import Keyword
from database.models.user import User
from database.tools import db_connection


@db_connection
async def add_key(session: AsyncSession, user_id: int, key: str):
    await session.execute(update(Key).where(Key.value == key)
                          .values(user_id=user_id))
    await session.commit()
