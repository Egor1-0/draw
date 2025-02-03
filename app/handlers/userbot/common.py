from asyncio import FastChildWatcher

from opentele.tl import TelegramClient
from opentele.api import API

from telethon import events
from utils.redis_serv import redis_serv
from utils.send_notification import send_notif

client = TelegramClient(
    'anon',
    API.TelegramDesktop.Generate(unique_id='+77079041946')
)


@client.on(events.NewMessage())
async def check_message(event):
    chat = await event.get_chat()
    chat_id = chat.id
    chats = await redis_serv.get_all_chats()

    if not str(chat_id) in list(chats.keys()):
        return

    keywords = await redis_serv.get_all_keywords()
    for keyword in keywords.keys():
        if keyword in event.text:
            if hasattr(event.chat, 'username') and event.chat.username:  # Проверяем наличие username у чата/канала
                post_link = f"https://t.me/{event.chat.username}/{event.message.id}"
            else:
                post_link = f"tg://privatepost?channel={chat_id}&post={event.message.id}"  # Для закрытых каналов/чатов

            await send_notif(user_id=keywords[keyword], text=f'Слово {keyword} использовалось в {post_link}')