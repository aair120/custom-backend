from pydantic_settings import BaseSettings, SettingsConfigDict
import asyncpg

class Settings(BaseSettings):
    db_name: str
    db_port: int
    db_host: str
    db_pass: str
    db_user: str

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()