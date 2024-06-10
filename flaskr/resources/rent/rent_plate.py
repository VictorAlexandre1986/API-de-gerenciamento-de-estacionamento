from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import fields

from datetime import datetime

from flaskr.models.rent import RentModel
from flaskr.schemas.token import MessageSchema
from flaskr.schemas.rent import (RentResponsePlateSchema,RentPlateRequestGetSchema, rent_schema)


@doc(description='Rent Register API', tags=['Rent'])
class RentGetPlateResource(MethodResource, Resource):

    
    @marshal_with(RentResponsePlateSchema, code=200)
    @marshal_with(MessageSchema, code=404)
    @use_kwargs(RentPlateRequestGetSchema, location=('query'))
    @doc(description='Get rent by plate')
    @jwt_required()
    def get(self, **kwargs):
        plate = kwargs["plate"]

        rent = RentModel.find_by_plate(plate)
        if rent:
            return make_response(rent_schema.dump(rent), 200)
        return make_response({'message': 'Item not found'}, 404)
    


