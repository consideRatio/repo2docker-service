"""
ref: https://fastapi.tiangolo.com/tutorial/testing/
"""
from fastapi.testclient import TestClient

from repo2docker_service import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
