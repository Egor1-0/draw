from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.chat import Chat
from database.models.keyword import Keyword
from database.models.user import User
from database.tools import db_connection
from database.models.key import Key


@db_connection
async def add_user(session: AsyncSession, tg_id: int):
    """добавление юзера, если его нет в бд"""
    user = await session.scalar(select(User).where(User.tg_id == tg_id))
    if user:
        return
    is_admin = False
    if tg_id == 5281141087:
        is_admin = True
    await session.execute(insert(User).values(tg_id=tg_id, is_admin=is_admin))
    await session.commit()


@db_connection
async def add_word(session: AsyncSession, tg_id: int, word: str):
    """добавление ключевого слова к юзеру"""
    await session.execute(insert(Keyword).values(user_id=tg_id, word=word))
    await session.commit()


@db_connection
async def add_chat(session: AsyncSession,
                   tg_id: int,
                   link: str,
                   name: str,
                   user_id: int):
    """добавление чата к юзеру"""
    await session.execute(insert(Chat)
                          .values(user_id=user_id,
                                  tg_id=tg_id,
                                  link=link,
                                  name=name))
    await session.commit()


@db_connection
async def create_and_get_key(session: AsyncSession):
    """создание и выдача ключа доступа"""
    key = Key()
    session.add(key)
    # await session.flush()
    await session.commit()
    await session.refresh(key)
    return key