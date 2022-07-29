import motor.motor_asyncio
from beanie import init_beanie
from src.config import settings
from src.users.models import User

# MONGO_CONFIG_URL=mongodb://root:mongoroot@mongo:27017/
MONGO_CONFIG_URL = f"mongodb://{settings.mongo_username}:{settings.mongo_password}@{settings.mongo_host}:{settings.mongo_port}/"


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_CONFIG_URL)
    await init_beanie(database=client.nmportal_db, document_models=[User])
