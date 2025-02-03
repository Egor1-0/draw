import os.path
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

_CONFIG_PATH = os.path.join(Path(__file__).parent.parent.parent, '.env')


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env' #Нужно для запуска через docker/docker compose
        # env_file=_CONFIG_PATH, #нужно для запуска через системд или python main.py
    )
