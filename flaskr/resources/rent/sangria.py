from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import fields

from datetime import datetime

from flaskr.models.rent import RentModel
from flaskr.schemas.token import MessageSchema
from flaskr.schemas.rent import (RentResponseDateSchema,RentDateRequestGetSchema, rent_schema)


@doc(description='Rent Register API', tags=['Rent'])
class RentSangriaRegisterResource(MethodResource, Resource):

   
    @marshal_with(RentResponseDateSchema, code=200)
    @marshal_with(MessageSchema, code=404)
    @use_kwargs(RentDateRequestGetSchema, location=('query'))
    @doc(description='Get rent by date')
    @jwt_required()
    def get(self, **kwargs):
        date = kwargs["date"]
        #Receber a data sem as horas para buscar todos os registros daquele dia
        rents = RentModel.find_by_date(date).all()
        if rents:
            total=0
            # return make_response(rent_schema.dump(rent), 200)
            for rent in rents:
                obj = rent_schema.dump(rent)
                saida = obj['rent_date_final'] = datetime.strptime(obj['rent_date_final'], '%Y-%m-%dT%H:%M:%S')
                entrada = obj['rent_date_initial'] = datetime.strptime(obj['rent_date_initial'], '%Y-%m-%dT%H:%M:%S')
                total_minutes = (saida - entrada).total_seconds() / 60
                total_a_receber = total_minutes * 0.125
                total+=total_a_receber
            return make_response({"total_recebido_no_mes ": total}, 200)
        return make_response({'message': 'Item not found'}, 404)
    
    
