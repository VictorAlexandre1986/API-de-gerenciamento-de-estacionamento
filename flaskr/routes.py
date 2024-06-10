from flask_restful import Api

from flaskr.resources.token import TokenRefresherResource, TokenResource
from flaskr.resources.user import UserRegisterResource
from flaskr.resources.resource.rent import RentRegisterResource
from flaskr.resources.resource.rent_plate import RentGetPlateResource
from flaskr.resources.resource.rent_date import RentGetDateRegisterResource



def config_app_routes(app, docs):
    api = Api(app)
    __setting_route_doc(UserRegisterResource, '/user', api, docs)
    __setting_route_doc(RentRegisterResource, '/rent', api, docs)
    __setting_route_doc(RentGetPlateResource, '/rent/plate', api, docs)
    __setting_route_doc(RentGetDateRegisterResource, '/rent/date', api, docs)
    __setting_route_doc(TokenResource, '/token', api, docs)
    __setting_route_doc(TokenRefresherResource, '/token/refresh', api, docs)
    return api


def __setting_route_doc(resource, route, api, docs):
    # Config routes
    api.add_resource(resource, route)
    # Add API in Swagger Documentation
    docs.register(resource)
