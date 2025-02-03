from aiogram import Bot

from config import config


async def send_notif(user_id: int, text):
    async with Bot(token=config.bot.token.get_secret_value()) as bot:
        try:
            await bot.send_message(chat_id=user_id, text=text)
        except:
            pass