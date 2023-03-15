import pytest


def test_login():
    assert False


test_inputs = [
    (
        {
            "email": None,
            "first_name": "foo",
            "last_name": "bar",
            "password": "password",
        },
        422,
        "email is a required value",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": None,
            "last_name": "j",
            "password": "password",
        },
        422,
        "first_name is a required value",
    ),
    (
        {
            "email": "j2@j.j",
            "first_name": "j",
            "last_name": None,
            "password": "password",
        },
        422,
        "last_name is a required value",
    ),
    (
        {
            "email": "j3@j.j",
            "first_name": "j",
            "last_name": "j",
            "password": None,
        },
        422,
        "password is a required value",
    ),
    (
        {
            "email": "jp@pj.yo",
            "first_name": "foo",
            "last_name": "bar",
            "password": "password",
        },
        200,
        "valid fields should pass",
    ),
    (
        {
            "email": "duplicate@test.test",
            "first_name": "duplicate",
            "last_name": "duplicate",
            "password": "password",
        },
        409,
        "duplicate records should return a conflict status code",
    ),
]


@pytest.mark.parametrize("body, status_code, msg", test_inputs)
def test_register(client, body, status_code, msg):
    if body.get("first_name") == "duplicate":
        client.post("/register", json=body)

    res = client.post("/register", json=body)
    assert res.status_code == status_code, msg


def test_reset_password():
    assert False
