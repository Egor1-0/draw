from redis.asyncio import Redis


class RedisService:
    def __init__(self, host='localhost', port=6379):
        self.r = Redis(host=host, port=port, decode_responses=True)

    async def set_chat_user(self, chat_id: int, user_id: int):
        """Добавляет пользователя в чат."""
        chat_key = f"chat:{chat_id}"
        await self.r.sadd(chat_key, user_id)

    async def get_chat_users(self, chat_id: int):
        """Получает всех пользователей из чата."""
        chat_key = f"chat:{chat_id}"
        return await self.r.smembers(chat_key)

    async def get_all_chats(self):
        """Получает все чаты."""
        chat_keys = await self.r.keys("chat:*")
        chats = {}
        for key in chat_keys:
            chat_id = key.split(":")[1]
            users = await self.r.smembers(key)
            chats[int(chat_id)] = list(users)
        return chats

    async def set_keyword_user(self, keyword: str, user_id: int):
        """Добавляет пользователя к ключевому слову."""
        keyword_key = f"keyword:{keyword}"
        await self.r.sadd(keyword_key, user_id)

    async def get_keyword_users(self, keyword: str):
        """Получает всех пользователей по ключевому слову."""
        keyword_key = f"keyword:{keyword}"
        return await self.r.smembers(keyword_key)

    async def get_all_keywords(self):
        """Получает все ключевые слова."""
        keyword_keys = await self.r.keys("keyword:*")
        keywords = {}
        for key in keyword_keys:
            keyword = key.split(":")[1]
            users = await self.r.smembers(key)
            keywords[keyword] = list(users)
        return keywords

    async def get_user_by_chat_and_keyword(self, chat_id: int, keyword: str):
        """Получает пользователей, которые находятся в чате и связаны с ключевым словом."""
        chat_key = f"chat:{chat_id}"
        keyword_key = f"keyword:{keyword}"

        chat_users = await self.r.smembers(chat_key)
        keyword_users = await self.r.smembers(keyword_key)

        common_users = chat_users.intersection(keyword_users)
        return list(common_users)

    async def remove_chat_user(self, chat_id: int, user_id: int):
        """Удаляет пользователя из чата."""
        chat_key = f"chat:{chat_id}"
        await self.r.srem(chat_key, user_id)

    async def remove_keyword_user(self, keyword: str, user_id: int):
        """Удаляет пользователя от ключевого слова."""
        keyword_key = f"keyword:{keyword}"
        await self.r.srem(keyword_key, user_id)

    async def remove_chat(self, chat_id: int):
        """Удаляет чат и всех пользователей в нем."""
        chat_key = f"chat:{chat_id}"
        await self.r.delete(chat_key)

    async def remove_keyword(self, keyword: str):
        """Удаляет ключевое слово и всех пользователей, связанных с ним."""
        keyword_key = f"keyword:{keyword}"
        await self.r.delete(keyword_key)

    async def clear_all_data(self):
        """Очищает все данные в Redis."""
        await self.r.flushdb()
        print("Все данные в Redis очищены.")


redis_serv = RedisService()
