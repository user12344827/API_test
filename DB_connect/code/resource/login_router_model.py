from marshmallow import Schema, fields

class RegisterSchema(Schema):
    name = fields.Str(required=True, description="User name")
    account = fields.Str(required=True, description="User account")
    password = fields.Str(required=True, description="User password")

class RegisterResponse(Schema):
    status = fields.Boolean(required=True)
    message = fields.Str()

class LoginSchema(Schema):
    account = fields.Str(doc="account", example="string", required=True)
    password = fields.Str(doc="password", example="string", required=True)

class LoginResponse(Schema):
    message = fields.Str(example="success")
    datatime = fields.Str(example="1970-01-01T00:00:00.000000")
    data = fields.Str(example="")