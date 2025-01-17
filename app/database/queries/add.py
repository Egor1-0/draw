from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.user import User
from database.tools import db_connection


@db_connection
async def add_user(session: AsyncSession, tg_id: int):
    await session.execute(insert(User).values(tg_id=tg_id))
    await session.commit()
