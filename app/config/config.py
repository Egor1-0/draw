from pydantic import BaseModel

from config.bot_config import BotConfig, bot_config
from config.database_config import DatabaseConfig, database_config


class AppConfig(BaseModel):
    bot: BotConfig
    database: DatabaseConfig


config = AppConfig(bot=bot_config, database=database_config)
