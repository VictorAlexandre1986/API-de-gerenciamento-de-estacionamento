from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import fields

from flaskr.utils.log import logging

from datetime import datetime

from flaskr.models.rent import RentModel
from flaskr.schemas.token import MessageSchema
from flaskr.schemas.rent import (RentResponseDateSchema,RentDateRequestGetSchema, rent_schema)


@doc(description='Rent Register API', tags=['Rent'])
class RentGetDateRegisterResource(MethodResource, Resource):

   
    @marshal_with(RentResponseDateSchema, code=200)
    @marshal_with(MessageSchema, code=404)
    @use_kwargs(RentDateRequestGetSchema, location=('query'))
    @doc(description='Get rent by date')
    @jwt_required()
    def get(self, **kwargs):
        date = kwargs["date"]

        rent = RentModel.find_by_date(date).all()
        if rent:
            logging.info('Rent found by date')
            return make_response(rent_schema.dump(rent), 200)
        logging.error('Rent not found by date')
        return make_response({'message': 'Item not found'}, 404)
    
    
