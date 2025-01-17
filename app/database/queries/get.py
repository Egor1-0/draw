from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from database.models.keyword import Keyword
from database.models.user import User
from database.tools import db_connection


@db_connection
async def get_user(session: AsyncSession, tg_id: int):
    return await session.scalar(select(User)
                                .where(User.tg_id == tg_id)
                                .join(Keyword, isouter=True)
                                .options(selectinload(User.words)))
