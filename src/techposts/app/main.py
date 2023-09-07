from fastapi import FastAPI

from techposts.core.config import config
from techposts.core.database.session import Engine
from techposts.core.helpers.health_check import (
    HealthModel,
    HealthResponse,
    HealthStatusError,
    get_mongo_status,
)


def create_app() -> FastAPI:
    app = FastAPI()

    return app


app = create_app()


@app.get("/")
async def root_path() -> dict[str, str]:
    return {"message": f"Welcome to {config.app_name}: v{config.version}"}


@app.get(
    "/health",
    tags=["health"],
    response_model=HealthResponse,
    responses={500: {"model": HealthStatusError}},
)
async def health_check() -> HealthResponse:
    """***Return Health check status.***"""

    resource_items = []
    resource_items += await get_mongo_status()
    total_status = all(key.status for key in resource_items)

    response_code = 200 if total_status else 500
    content = HealthModel(
        name=config.app_name,
        status=total_status,
        version=config.version,
        resources=resource_items,
    )

    return HealthResponse(status_code=response_code, health_model=content)


@app.on_event("startup")
async def create_db_client() -> None:
    """Initialize DB connection."""

    await Engine.connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_db_client() -> None:
    """Close DB connection."""

    await Engine.close_mongo_connection()
