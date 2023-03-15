from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_login():
    assert False


def test_register():
    assert False


def test_reset_password():
    assert False
