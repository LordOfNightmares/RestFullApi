from flask_jwt import jwt_required
from flask_restful import Resource


class AuthenticatedResource(Resource):
    method_decorators = [jwt_required()]
