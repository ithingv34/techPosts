from typing import Type, TypeVar

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from techposts.core.config import config

T = TypeVar("T", bound="Engine")


class Engine:
    """MongoDb database async engine class.


    :type db: C{motor.motor_asyncio.AsyncIOMotorDatabase}
    :ivar db: AsyncIOMotorDatabase class instance.
    :type connection: C{motor.motor_asyncio.AsyncIOMotorClient}
    :ivar connection: AsyncIOMotorClient class instance.
    """

    db: AsyncIOMotorDatabase = None
    connection: AsyncIOMotorClient = None

    @classmethod
    async def connect_to_mongo(cls: Type[T]) -> None:
        """Initialize DB connection to MongoDb and database."""

        cls.connection = AsyncIOMotorClient(
            config.db_url, serverSelectionTimeoutMS=5000
        )
        cls.db = cls.connection.api_db

    @classmethod
    async def close_mongo_connection(cls: Type[T]) -> None:
        """Close DB connection."""

        cls.connection.close()
