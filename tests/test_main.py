from ..main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_healthcheck():
    res = client.get("/health")
    res.status_code == 200
    res.data = {"status": "online"}
