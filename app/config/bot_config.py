from pydantic import SecretStr

from config.base import BaseConfig


class BotConfig(BaseConfig):
    token: SecretStr
    api_id: int
    api_hash: str

bot_config = BotConfig()
