from pydantic_settings import BaseSettings
from dotenv import find_dotenv
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Clients API"
    mongodb_url: str
    db_name: str

    class Config:
        env_file = find_dotenv(".env")
        env_file_encoding = "utf-8"


@lru_cache
def get_settings():
    return Settings()