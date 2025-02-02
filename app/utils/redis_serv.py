from asyncio import FastChildWatcher

from redis.asyncio import Redis


class RedisService:
    def __init__(self, host='localhost', port=6379):
        self.r = Redis(host=host, port=port, decode_responses=True)
        self.chat_key = 'chats'
        self.keyword_key = 'keyword'

    async def set_chat(self, chat_id: int, user_id: int):
        await self.r.hset(self.chat_key, str(chat_id), str(user_id))

    async def get_chat(self, chat_id: int):
        user_id = await self.r.hget(self.chat_key, str(chat_id))
        return user_id

    async def get_all_chats(self):
        return await self.r.hgetall(self.chat_key)

    async def remove_chat(self, chat_id: int):
        await self.r.hdel(self.chat_key, str(chat_id))

    async def set_keyword(self, keyword: str, user_id: int):
        await self.r.hset(self.keyword_key, str(keyword), str(user_id))

    async def get_keyword(self, keyword: str):
        user_id = await self.r.hget(self.keyword_key, keyword)
        return user_id

    async def get_all_keywords(self):
        return await self.r.hgetall(self.keyword_key)

    async def remove_keyword(self, keyword: str):
        await self.r.hdel(self.keyword_key, keyword)



redis_serv = RedisService()
