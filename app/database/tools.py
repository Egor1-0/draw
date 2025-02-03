from sqlalchemy.ext.asyncio import AsyncSession
from cuid import cuid

from database.core import async_session, engine
from database.models.base import Base


class DbConnection():
    def __init__(self, async_session: AsyncSession):
        self._async_session = async_session

    def __call__(self, func):
        """функция для доступа к асинхронной сессии в запросах к бд. используется как декоратор"""
        async def wrapper(*args, **kwargs):
            async with self._async_session() as session:
                return await func(session, *args, **kwargs)

        return wrapper


async def create_table():
    async with engine.begin() as conn:
        """создание таблиц"""
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


def _generate_cuid():
    """генерация ключа доступа"""
    return cuid()


db_connection = DbConnection(async_session=async_session)
