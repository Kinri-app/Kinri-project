# app/user/schemas.py

from marshmallow import Schema, fields, validate, ValidationError


class RegisterSchema(Schema):
    email = fields.Email(
        required=True,
        error_messages={"required": "Email is required", "invalid": "Invalid email format"}
    )
    password = fields.Str(
        required=True,
        validate=validate.Length(min=8),
        error_messages={"required": "Password is required", "invalid": "Invalid password"}
    )


class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class UpdateUserSchema(Schema):
    email = fields.Email(required=False)
    password = fields.Str(required=False, validate=validate.Length(min=8))

