import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="session", name="client")
def client():
    client = TestClient(app)
    return client
