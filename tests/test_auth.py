import pytest
from .data import invalid_register_input

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
