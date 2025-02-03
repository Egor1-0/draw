from pydantic import BaseModel

from config.bot_config import BotConfig, bot_config
from config.database_config import DatabaseConfig, database_config
from config.redis_config import RedisConfig, redis_config


class AppConfig(BaseModel):
    bot: BotConfig
    database: DatabaseConfig
    redis: RedisConfig

config = AppConfig(bot=bot_config, database=database_config, redis=redis_config)
