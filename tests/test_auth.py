import pytest


# def test_login():
#     assert False


invalid_register_input = [
    (
        {
            "email": None,
            "first_name": "foo",
            "last_name": "bar",
            "password": "password",
        },
        {
            "status_code": 422,
            "loc": ["body", "email"],
            "msg": "type_error.none.not_allowed",
        },
        "email is a required value",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": None,
            "last_name": "j",
            "password": "password",
        },
        {
            "status_code": 422,
            "loc": ["body", "first_name"],
            "type": "type_error.none.not_allowed",
        },
        "first_name is a required value",
    ),
    (
        {
            "email": "j2@j.j",
            "first_name": "j",
            "last_name": None,
            "password": "password",
        },
        {
            "status_code": 422,
            "loc": ["body", "last_name"],
            "type": "type_error.none.not_allowed",
        },
        "last_name is a required value",
    ),
    (
        {
            "email": "j3@j.j",
            "first_name": "j",
            "last_name": "j",
            "password": None,
        },
        {
            "status_code": 422,
            "loc": ["body", "password"],
            "type": "type_error.none.not_allowed",
        },
        "password is a required value",
    ),
    (
        {
            "email": "valid@email.com",
            "first_name": "duplicate",
            "last_name": "duplicate",
            "password": "password",
        },
        {"status_code": 409, "type": "duplicate_email"},
        "duplicate records should return a conflict status code",
    ),
    (
        {
            "email": "invalid email",
            "first_name": "foo",
            "last_name": "bar",
            "password": "password",
        },
        {"status_code": 409, "type": "value_error.email"},
        "email should have appropriate formatting",
    ),
]


@pytest.mark.parametrize("body, expected, msg", invalid_register_input)
def test_register_invalid_input(client, body, expected, msg):
    # TODO: remove this if statement and add a record in a fixture
    if body.get("first_name") == "duplicate":
        client.post("/register", json=body)

    res = client.post("/register", json=body)
    assert res.status_code == expected["status_code"], msg

    detail = res.json()["detail"][0]
    assert detail["loc"] == expected["loc"]
    assert expected["type"] in detail["type"]


valid_register_input = [
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
]


# @pytest.mark.parametrize("body, status_code, msg", valid_register_input)
# def test_register_valid_input(client, body, status_code, msg):
#     # TODO: remove this if statement and add a record in a fixture
#     if body.get("first_name") == "duplicate":
#         client.post("/register", json=body)

#     res = client.post("/register", json=body)
#     assert res.status_code == status_code, msg

#     if res.status_200 != 200:
#         assert (
#             res.json["value_error.any_str.min_length"]
#             == "value_error.any_str.min_length"
#         )


# def test_reset_password():
#     assert False
