import pytest
import re
from .data import invalid_register_input, valid_register_input

# def test_login():
#     assert False


@pytest.mark.parametrize("body, expected, msg", invalid_register_input)
def test_register_invalid_input(client, body, expected, msg):
    # TODO: remove this if statement and add a record in a fixture
    if body.get("first_name") == "duplicate":
        client.post("/register", json=body)
    res = client.post("/register", json=body)
    assert res.status_code == expected["status_code"], msg

    detail = res.json()["detail"][0]
    assert detail["loc"] == expected["loc"], msg

    if expected.get("type"):
        assert expected["type"] in detail["type"], msg

    if expected.get("msg"):
        assert expected["msg"] in detail["msg"], msg


@pytest.mark.parametrize("body, expected, msg", valid_register_input)
def test_register_valid_input(client, body, expected, msg):
    res = client.post("/register", json=body)
    assert res.status_code == expected["status_code"], msg

    try:
        jwt_regex = re.compile(r"^[A-Za-z0-9_-]{2,}(?:\.[A-Za-z0-9_-]{2,}){2}$")
    except re.errors() as e:
        raise e

    res_body = res.json()
    assert jwt_regex.fullmatch(res_body["access_token"]), msg
    assert res_body["token_type"] == "bearer", msg
    # TODO: add check that token contains sub with id
    # TODO: add check that id matches id of user in DB


# def test_reset_password():
#     assert False
