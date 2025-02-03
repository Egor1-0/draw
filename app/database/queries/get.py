from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from database.models.chat import Chat
from database.models.key import Key
from database.models.keyword import Keyword
from database.models.user import User
from database.tools import db_connection


@db_connection
async def get_user(session: AsyncSession, tg_id: int):
    """получение юзера из бд по тг айди"""
    return await session.scalar(select(User)
                                .where(User.tg_id == tg_id)
                                .options(selectinload(User.words),
                                         selectinload(User.chats),
                                         selectinload(User.key))
                                )


@db_connection
async def get_key(session: AsyncSession, key: str):
    """получение ключа доступа из бд по значению"""
    return await session.scalar(select(Key)
                                .where(Key.value == key)
                                .options(selectinload(Key.user))
                                )


@db_connection
async def get_keyword_by_id(session: AsyncSession, kw_id: int):
    """получение ключевого слова из бд по айди из бд"""
    return await session.scalar(select(Keyword)
                                .where(Keyword.id == kw_id)
                                )


@db_connection
async def get_chat_by_id(session: AsyncSession, chat_id: int):
    """получение чата по айди из бд"""
    return await session.scalar(select(Chat)
                            .where(Chat.id == chat_id)
                            )