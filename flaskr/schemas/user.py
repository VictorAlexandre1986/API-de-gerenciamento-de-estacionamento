from marshmallow import Schema, fields

from flaskr.schema import ma


class UserResponseSchema(ma.Schema):
    id = fields.Int()
    username = fields.Str()
    class Meta:
        # Fields to expose
        fields = ("id", "username")
        ordered = True

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("user")
        }
    )

class UserRequestPostSchema(Schema):
    username = fields.Str(required=True, default='user1', help='This field cannot be blank')
    password = fields.Str(required=True, default='pwd1', help='This field cannot be blank')

class UserRequestGetSchema(Schema):
    uid = fields.Int(required=True, default='id', help='Invalid id')


user_schema = UserResponseSchema()
