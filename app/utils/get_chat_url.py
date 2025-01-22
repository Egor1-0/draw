import re

from aiogram.types import Message


def get_telegram_link(message: Message):
    pattern = r'^https?://t\.me/(?:\+[a-zA-Z0-9_-]+|joinchat/[a-zA-Z0-9_-]+|[a-zA-Z0-9_]+/?)$'
    entities = message.entities or []

    try:
        for item in entities:
            if item.type == 'url':
                url = item.extract_from(message.text)
                if bool(re.match(pattern, url)):
                    return url
    except:
        pass
    return