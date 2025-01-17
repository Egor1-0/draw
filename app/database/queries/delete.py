from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.keyword import Keyword
from database.tools import db_connection


@db_connection
async def delete_word(session: AsyncSession, word_id: int):
    await session.execute(delete(Keyword).where(Keyword.id == word_id))
    await session.commit()