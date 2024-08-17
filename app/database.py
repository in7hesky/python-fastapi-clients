from motor.motor_asyncio import AsyncIOMotorClient
from .config import get_settings

def get_database_client():
    return AsyncIOMotorClient(get_settings().mongodb_url)
