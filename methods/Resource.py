from flask_restful import Resource
from flask_jwt import jwt_required


class AuthenticatedResource(Resource):
    method_decorators = [jwt_required()]
