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
    """мониторинг чатов и отправка уведомлений по ключевым словам"""
    chat = await event.get_chat()
    chat_id = chat.id
    chats = await redis_serv.get_all_chats()
    # print('chats', chats)
    if not chat_id in list(chats.keys()):
        return

    keywords = await redis_serv.get_all_keywords()
    # print('kw', keywords)
    for keyword in keywords.keys():
        if keyword.lower() in event.text.lower():
            if hasattr(event.chat, 'username') and event.chat.username:
                post_link = f"https://t.me/{event.chat.username}/{event.message.id}"
            else:
                post_link = f"tg://privatepost?channel={chat_id}&post={event.message.id}"
            users = await redis_serv.get_user_by_chat_and_keyword(chat_id=chat_id, keyword=keyword)
            print('users', users)
            for user in users:
                await send_notif(user_id=user, text=f'Слово {keyword} использовалось в {post_link}')