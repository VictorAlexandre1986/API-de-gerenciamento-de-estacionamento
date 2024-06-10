from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import fields

from flaskr.models.user import UserModel
from flaskr.schemas.token import MessageSchema
from flaskr.schemas.user import (UserRequestGetSchema, UserRequestPostSchema,
                                 UserResponseSchema, user_schema)


@doc(description='User Register API', tags=['User'])
class UserRegisterResource(MethodResource, Resource):

    @marshal_with(UserResponseSchema, code=201)
    @marshal_with(MessageSchema, code=400)
    @use_kwargs(UserRequestPostSchema, location=('json'))
    @doc(description='Register a new user')
    def post(self, **kwargs):
        if UserModel.find_by_username(kwargs['username']):
            return make_response({"message": "Username already exists"}, 400)

        user = UserModel(**kwargs)
        user.save()

        return make_response(user_schema.dump(user), 201)

    @use_kwargs(
    {
        'Authorization':
        fields.Str(
            required=True,
            description='Bearer [access_token]'
        )
    }, location=('headers'))
    
    @marshal_with(UserResponseSchema, code=201)
    @marshal_with(MessageSchema, code=404)
    @use_kwargs(UserRequestGetSchema, location=('query'))
    @doc(description='Get user by id')
    @jwt_required()
    def get(self, **kwargs):
        user_id = kwargs["uid"]

        user = UserModel.find_by_id(user_id)
        if user:
            return make_response(user_schema.dump(user), 200)
        return make_response({'message': 'Item not found'}, 404)
    
    @marshal_with(UserResponseSchema, code=200)
    @marshal_with(MessageSchema, code=404)
    @use_kwargs(UserRequestPostSchema, location=('json'))
    @doc(description='Update user by id')
    @jwt_required()
    def put(self, **kwargs):
        user_id = kwargs["id"]

        user = UserModel.find_by_id(user_id)
        if not user:
            return make_response({'message': 'User not found'}, 404)

        user.update(**kwargs)
        return make_response(user_schema.dump(user), 200)

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
    @use_kwargs(UserRequestGetSchema, location=('query'))
    @doc(description='Delete user by id')
    @jwt_required()
    def delete(self, **kwargs):
        user_id = kwargs["uid"]

        user = UserModel.find_by_id(user_id)
        if not user:
            return make_response({'message': 'User not found'}, 404)

        user.delete()
        return make_response({'message': 'User deleted'}, 200)
