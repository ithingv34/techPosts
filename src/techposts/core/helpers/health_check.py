from typing import List

from loguru import logger
from pydantic import BaseModel, Field

from techposts.core.config import config
from techposts.core.database.session import Engine

# from docs.openapi_documentation import resource_example


resource_example = [{"name": "MongoDB", "status": True}]


class HealthStatusError(BaseModel):
    """Define model for a http 500 exception (INTERNAL_SERVER_ERROR)."""

    detail: str = "HEALTH: database connection is down"


class ResourceModel(BaseModel):
    """Define OpenAPI model for a health resources response.

    :ivar name: Resource name.
    :ivar status: Resource status
    """

    name: str
    status: bool


class HealthModel(BaseModel):
    """Define OpenAPI model for a health response.

    :ivar name: Service name.
    :ivar status: Overall health status
    :ivar version: Service version.
    :ivar resources: Status for individual resources..
    """

    status: bool
    name: str = Field(example=config.app_name)
    version: str = Field(example=config.version)
    resources: List[ResourceModel] = Field(example=resource_example)


class HealthResponse(BaseModel):
    status_code: int
    health_model: HealthModel


async def get_mongo_status() -> List[ResourceModel]:
    """Return MongoDb connection status.

    :return: MongoDb connection status.
    """

    try:
        await Engine.connection.server_info()
        status = True

    except BaseException as why:
        logger.critical(f"MongoDB: {why}")
        status = False

    return [ResourceModel(name="MongoDb", status=status)]
