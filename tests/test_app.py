"""
ref: https://fastapi.tiangolo.com/tutorial/testing/
"""

from fastapi.testclient import TestClient

from repo2docker_service import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200


def test_read_root_index():
    response = client.get("/index.html")
    assert response.status_code == 200


def test_read_builds():
    response = client.get("/builds/")
    assert response.status_code == 200
