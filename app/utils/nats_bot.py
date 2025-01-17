import asyncio

from aiogram import Bot
from nats.js import JetStreamContext
from nats.aio.client import Client, Msg

from config import ADMIN_ID

class Nats:
    def __init__(self, nc: Client, js: JetStreamContext, bot: Bot):
        self.nc = nc
        self.js = js
        self.bot = bot

    async def get_webhook(self):
        psub = await self.js.pull_subscribe(stream='', subject='', durable='')
        while True:
            try:
                msgs = await psub.fetch(1)
                for msg in msgs:
                    try:
                        pass
                    except Exception as e:
                        print(e)
                    finally:
                        await msg.ack()
            except TimeoutError:
                continue

async def init_nats_bot(bot: Bot, nc: Client, js: JetStreamContext):
    nats_bot = Nats(nc, js, bot)
    asyncio.create_task(nats_bot.get_webhook())

        