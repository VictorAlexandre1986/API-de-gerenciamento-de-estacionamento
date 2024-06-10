from marshmallow import Schema, fields

from flaskr.schema import ma


class RentResponseSchema(ma.Schema):
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


class RentResponsePlateSchema(ma.Schema):
    rent = fields.Str(required=True, default='plate', help='Invalid plate')

class RentResponseDateSchema(ma.Schema):
    rent = fields.DateTime(required=True, default='date', help='Invalid date')

class RentRequestPostSchema(Schema):
    username = fields.Str(required=True, default='user1', help='This field cannot be blank')
    password = fields.Str(required=True, default='pwd1', help='This field cannot be blank')
    plate = fields.Str(required=True, default='plate', help='This field cannot be blank')
    model = fields.Str(required=True, default='model', help='This field cannot be blank')
    rent_date_initial = fields.DateTime(required=True, default='2020-01-01', help='This field cannot be blank')
    rent_date_final = fields.DateTime(required=False, default=None)
    total = fields.Int(required=False, default=0)

class RentRequestGetSchema(Schema):
    uid = fields.Int(required=True, default='id', help='Invalid id')

class RentPlateRequestGetSchema(Schema):
    plate = fields.String(required=True, default='plate', help='Invalid plate')

class RentDateRequestGetSchema(Schema):
    date = fields.DateTime(required=True, default='date', help='Invalid date')


rent_schema = RentResponseSchema()
