from asyncio import FastChildWatcher

from opentele.tl import TelegramClient
from opentele.api import API

from telethon import events
from utils.redis_serv import redis_serv

client = TelegramClient(
    'anon',
    API.TelegramDesktop.Generate(unique_id='+77079041946')
)


@client.on(events.NewMessage())
async def check_message(event):
    chat = await event.get_chat()
    chat_id = chat.id
    chats = await redis_serv.get_all_chats()
    print(chat_id, list(chats.keys()))
    if not chat_id in list(chats.keys()):
        return
    print(2)
    keywords = await redis_serv.get_all_keywords()
    print(keywords)
    for keyword in keywords.keys():
        if keyword in chat.text:
            print(keyword)
