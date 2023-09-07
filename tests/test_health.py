import pytest
from httpx import AsyncClient
from starlette.testclient import TestClient

pytestmark = pytest.mark.anyio


async def test_normal_health(test_app: TestClient) -> None:
    """Test successful health endpoint.

    :param test_app: TestClient instance.
    """

    async with AsyncClient(app=test_app.app, base_url="http://test") as client:
        response = await client.get("/health")

    assert response.json()["status_code"] == 200
    assert response.json()["health_model"]["status"] is True


async def test_health_error(test_app: TestClient) -> None:
    """Test failed health endpoint.

    :param test_app: TestClient instance.
    """

    async with AsyncClient(app=test_app.app, base_url="http://test") as client:
        response = await client.get("/health")

    assert response.json()["status_code"] == 500
    assert response.json()["health_model"]["status"] is False
