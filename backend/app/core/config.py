from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    alpaca_key: str
    alpaca_secret: str
    db_url: str = "sqlite:///./alpaca.db"
    redis_url: str = "redis://localhost:6379"
    rabbit_url: str = "amqp://guest:guest@localhost:5672/"
    openai_api_key: str | None = None
    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()
