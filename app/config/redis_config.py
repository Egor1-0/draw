from pydantic import SecretStr

from config.base import BaseConfig


class RedisConfig(BaseConfig):
    redis_host: str
    redis_port: int

redis_config = RedisConfig()
