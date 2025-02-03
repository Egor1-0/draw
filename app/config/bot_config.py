from pydantic import SecretStr

from config.base import BaseConfig


class BotConfig(BaseConfig):
    token: SecretStr

bot_config = BotConfig()
