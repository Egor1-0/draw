from pydantic import SecretStr
# from sqlalchemy import URL

from config.base import BaseConfig


class DatabaseConfig(BaseConfig):
    host: str
    port: int
    password: SecretStr
    user: str
    db_name: str

    def create_url(self):
        return 'sqlite+aiosqlite:///data/test.db'
        # return URL.create(
        #     drivername="postgresql+asyncpg",
        #     host=self.host,
        #     port=self.port,
        #     username=self.user,
        #     password=self.password.get_secret_value(),
        #     database=self.db_name,
        # )


database_config = DatabaseConfig()
