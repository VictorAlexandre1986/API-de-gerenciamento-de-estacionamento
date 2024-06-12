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
from flaskr.schemas.rent import (RentRequestGetSchema, RentRequestPostSchema,
                                 RentResponseSchema,RentDateRequestGetSchema,
                                 RentPlateRequestGetSchema, rent_schema)


@doc(description='Rent Register API', tags=['Rent'])
class RentRegisterResource(MethodResource, Resource):

    @marshal_with(RentResponseSchema, code=201)
    @marshal_with(MessageSchema, code=400)
    @use_kwargs(RentRequestPostSchema, location=('json'))
    @doc(description='Register a new rent')
    def post(self, **kwargs):
        if not RentModel.find_by_username(kwargs['username']):
            logging.error('Username no exists in database')
            return make_response({"message": "Username no exists"}, 400)

        rent = RentModel(**kwargs)
        rent.save()
        logging.info('Rent created')
        return make_response(rent_schema.dump(rent), 201)

    @use_kwargs(
    {
        'Authorization':
        fields.Str(
            required=True,
            description='Bearer [access_token]'
        )
    }, location=('headers'))
    
    @marshal_with(RentResponseSchema, code=201)
    @marshal_with(MessageSchema, code=404)
    @use_kwargs(RentRequestGetSchema, location=('query'))
    @doc(description='Get rent by id')
    @jwt_required()
    def get(self, **kwargs):
        rent_id = kwargs["uid"]

        rent = RentModel.find_by_id(rent_id)
        if rent:
            logging.info('Rent found by id in database')
            return make_response(rent_schema.dump(rent), 200)
        logging.error('Rent not found in database')
        return make_response({'message': 'Item not found'}, 404)
    
    
    @marshal_with(RentResponseSchema, code=200)
    @marshal_with(MessageSchema, code=404)
    @use_kwargs(RentRequestPostSchema, location=('json'))
    @doc(description='Update rent by id')
    @jwt_required()
    def put(self, **kwargs):
        user_id = kwargs["id"]

        user = RentModel.find_by_id(user_id)
        if not user:
            logging.error('Rent not found in update in database')
            return make_response({'message': 'Rent not found'}, 404)

        current_datetime = datetime.now()
        kwargs['rent_date_final'] = current_datetime
        kwargs['total'] = ((current_datetime - user.rent_date_initial).total_seconds() / 60 ) * 0.125
        user.update(**kwargs)
        logging.info('Rent updated in database')
        return make_response(rent_schema.dump(user), 200)

    @use_kwargs(
    {
        'Authorization':
        fields.Str(
            required=True,
            description='Bearer [access_token]'
        )
    }, location=('headers'))

    @marshal_with(MessageSchema, code=200)
    @marshal_with(MessageSchema, code=404)
    @use_kwargs(RentRequestGetSchema, location=('query'))
    @doc(description='Delete rent by id')
    @jwt_required()
    def delete(self, **kwargs):
        user_id = kwargs["uid"]

        user = RentModel.find_by_id(user_id)
        if not user:
            logging.error('Rent not found in delete in database')
            return make_response({'message': 'User not found'}, 404)

        user.delete()
        logging.info('Rent deleted in database')
        return make_response({'message': 'Rent deleted'}, 200)
