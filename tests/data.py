_invalid_email_input = [
    (
        {
            "email": None,
            "first_name": "foo",
            "last_name": "bar",
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "email"],
            "type": "type_error.none.not_allowed",
        },
        "email should not be 'None'",
    ),
    (
        {
            "first_name": "foo",
            "last_name": "bar",
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "email"],
            "type": "value_error.missing",
        },
        "email should not be missing",
    ),
    (
        {
            "email": "",
            "first_name": "foo",
            "last_name": "bar",
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "email"],
            "type": "value_error.email",
        },
        "email should not be an empty string",
    ),
    (
        {
            "email": "",
            "first_name": "foo",
            "last_name": "bar",
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "email"],
            "type": "value_error.email",
        },
        "email is a required value",
    ),
    (
        {
            "email": "invalid@email",
            "first_name": "foo",
            "last_name": "bar",
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "email"],
            "type": "value_error.email",
        },
        "email should have a valid format",
    ),
    (
        {
            "email": "invalid.email",
            "first_name": "foo",
            "last_name": "bar",
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "email"],
            "type": "value_error.email",
        },
        "email should have a valid format",
    ),
    (
        {
            "email": "valid@email.com",
            "first_name": "duplicate",
            "last_name": "duplicate",
            "password": "P@Ssword123",
        },
        {"status_code": 409, "loc": None, "type": "duplicate_email"},
        "duplicate records should return a conflict status code",
    ),
]
_invalid_first_name_input = [
    (
        {
            "email": "j@j.j",
            "first_name": None,
            "last_name": "j",
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "first_name"],
            "type": "type_error.none.not_allowed",
        },
        "first_name should not be none",
    ),
    (
        {
            "email": "j@j.j",
            "last_name": "bar",
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "first_name"],
            "type": "value_error.missing",
        },
        "first_name should not be missing",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "",
            "last_name": "bar",
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "first_name"],
            "type": "min_length",
        },
        "first_name should not be an empty string",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "a" * 33,
            "last_name": "bar",
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "first_name"],
            "type": "max_length",
        },
        "first_name should not be greater than 32 characters in length",
    ),
]
_invalid_last_name_input = [
    (
        {
            "email": "j@j.j",
            "first_name": "j",
            "last_name": None,
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "last_name"],
            "type": "type_error.none.not_allowed",
        },
        "last_name should not be none",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "foo",
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "last_name"],
            "type": "value_error.missing",
        },
        "last_name should not be missing",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "foo",
            "last_name": "",
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "last_name"],
            "type": "min_length",
        },
        "last_name should not be an empty string",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "foo",
            "last_name": "a" * 33,
            "password": "P@ssword123",
        },
        {
            "status_code": 422,
            "loc": ["body", "last_name"],
            "type": "max_length",
        },
        "last_name should not be greater than 32 characters in length",
    ),
]

_invalid_password_input = [
    (
        {
            "email": "j@j.j",
            "first_name": "j",
            "last_name": "j",
            "password": None,
        },
        {
            "status_code": 422,
            "loc": ["body", "password"],
            "type": "type_error.none.not_allowed",
        },
        "passowrd should not be none",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "foo",
            "last_name": "bar",
        },
        {
            "status_code": 422,
            "loc": ["body", "password"],
            "type": "value_error.missing",
        },
        "password should not be missing",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "foo",
            "last_name": "bar",
            "password": "",
        },
        {
            "status_code": 422,
            "loc": ["body", "password"],
            "type": "min_length",
        },
        "password should not be an empty string",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "foo",
            "last_name": "bar",
            "password": "@Fo0bar",
        },
        {
            "status_code": 422,
            "loc": ["body", "password"],
            "type": "min_length",
        },
        "password should not be less than 8 characters in length",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "foo",
            "last_name": "bar",
            "password": ("a" * 30) + "H0*",
        },
        {
            "status_code": 422,
            "loc": ["body", "password"],
            "type": "max_length",
        },
        "password should not be less than 32 characters in length",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "foo",
            "last_name": "bar",
            "password": ("a" * 8) + "@0",
        },
        {
            "status_code": 422,
            "loc": ["body", "password"],
            "msg": "1 uppercase",  # limitation of validator decorator
        },
        "password should contain a uppercase letter",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "foo",
            "last_name": "bar",
            "password": ("a" * 8) + "@H",
        },
        {
            "status_code": 422,
            "loc": ["body", "password"],
            "msg": "1 digit",  # limitation of validator decorator
        },
        "password should contain a number",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "foo",
            "last_name": "bar",
            "password": ("a" * 8) + "1H",
        },
        {
            "status_code": 422,
            "loc": ["body", "password"],
            "msg": "1 digit",  # limitation of validator decorator
        },
        "password should contain a symbol",
    ),
    (
        {
            "email": "j@j.j",
            "first_name": "foo",
            "last_name": "bar",
            "password": ("A" * 8) + "1@",
        },
        {
            "status_code": 422,
            "loc": ["body", "password"],
            "msg": "1 lowercase",  # limitation of validator decorator
        },
        "password should contain a lowercase letter",
    ),
]

invalid_register_input = [
    *_invalid_email_input,
    *_invalid_first_name_input,
    *_invalid_last_name_input,
    *_invalid_password_input,
]
