from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from database.models.key import Key
from database.models.keyword import Keyword
from database.models.user import User
from database.tools import db_connection


@db_connection
async def get_user(session: AsyncSession, tg_id: int):
    return await session.scalar(select(User)
                                .where(User.tg_id == tg_id)
                                .options(selectinload(User.words),
                                         selectinload(User.chats),
                                         selectinload(User.key))
                                )


@db_connection
async def get_key(session: AsyncSession, key: str):
    return await session.scalar(select(Key)
                                .where(Key.value == key)
                                .options(selectinload(Key.user))
                                )


@db_connection
async def get_keyword_by_id(session: AsyncSession, kw_id: int):
    return await session.scalar(select(Keyword)
                                .where(Keyword.id == kw_id)
                                )
