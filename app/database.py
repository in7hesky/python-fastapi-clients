from motor.motor_asyncio import AsyncIOMotorClient
from .config import get_settings

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(get_settings().mongodb_url)
        self.db = self.client[get_settings().db_name]
        self.clients_collection = self.db['clients']