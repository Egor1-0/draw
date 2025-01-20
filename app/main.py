import asyncio
import logging

# from nats import connect
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from telethon import TelegramClient

from config import config
from handlers.user import user_router
from database.tools import create_table


async def main():
    await create_table()


    bot = Bot(token=config.bot.token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    dp = Dispatcher()

    # nc = await connect('nats://nats:4222')
    # js = nc.jetstream()
    # await init_nats_bot(bot, nc, js)

    # client = TelegramClient('acc', config.bot.api_id, config.bot.api_hash)
    #
    # await client.start()

    client = None

    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(user_router)

    await dp.start_polling(bot, userbot=client)

    # client.disconnect()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s | %(levelname)s | %(message)s')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
