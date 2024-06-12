from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import fields

from flaskr.utils.log import logging

from flaskr.models.user import UserModel
from flaskr.schemas.token import MessageSchema
from flaskr.schemas.user import (UserResponseSchema, user_schema)


@doc(description='User Get All API', tags=['User'])
class UserGetAllResource(MethodResource, Resource):

    @marshal_with(UserResponseSchema(many=True), code=200)
    @marshal_with(MessageSchema, code=404)
    @doc(description='Get users all')
    @jwt_required()
    def get(self):

        user = UserModel.find_all()
        if user:
            logging.info('List of users found')
            return make_response(user_schema.dump(user), 200)
        logging.error('Users not found')
        return make_response({'message': 'Itens not found'}, 404)