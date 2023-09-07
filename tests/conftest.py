from typing import Generator

import pytest
from starlette.testclient import TestClient

from techposts.app.main import app


@pytest.fixture(scope="module")
def anyio_backend() -> str:
    """Module fixture."""

    return "asyncio"


@pytest.fixture(scope="module")
def test_app() -> Generator:
    with TestClient(app) as test_client:
        yield test_client
