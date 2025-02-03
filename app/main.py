import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from config import config
from handlers.user import user_router
from handlers.admin import admin_router
from database.tools import create_table


async def main():
    """запуск бота и базовые действия"""
    await create_table()
    # from utils.redis_serv import redis_serv
    # await redis_serv.clear_all_data()

    bot = Bot(token=config.bot.token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    dp = Dispatcher()

    from handlers.userbot.common import client
    await client.start()


    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(admin_router, user_router)

    await dp.start_polling(bot, userbot=client)

    client.disconnect()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s | %(levelname)s | %(message)s')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
