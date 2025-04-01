from marshmallow import Schema, fields

# Request

class UserGetSchema(Schema):
    name = fields.Str(doc="name", example="string", required=True)
    gender = fields.Str(doc="gender", example="string", required=True)
    birth = fields.Str(doc="birth", example="string", required=True)
    note = fields.Str(doc="note", example="string", required=True)

class UserPutSchema(Schema):
    name = fields.Str(doc="name", example="string", required=True)
    gender = fields.Str(doc="gender", example="string", required=True)
    birth = fields.Str(doc="birth", example="string", required=True)
    note = fields.Str(doc="note", example="string", required=True)


class UserPostSchema(Schema):
    name = fields.Str(doc="name", example="string", required=True)
    gender = fields.Str(doc="gender", example="string", required=True)
    birth = fields.Str(doc="birth", example="string", required=True)
    note = fields.Str(doc="note", example="string", required=True)


# Response
class UserGetResponse(Schema):
    message = fields.Str(example="success")
    datatime = fields.Str(example="1970-01-01T00:00:00.000000")
    data = fields.List(fields.Dict())


class UserSingleGetResponse(Schema):
    message = fields.Str(example="success")
    datatime = fields.Str(example="1970-01-01T00:00:00.000000")
    data = fields.Dict()


class UserPostResponse(Schema):
    message = fields.Str(example="success")


class UserPutResponse(Schema):
    message = fields.Str(example="success")


class UserSingleDeleteResponse(Schema):
    message = fields.Str(example="success")