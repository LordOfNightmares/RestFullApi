from flask_restful import Resource
from app import jwt_required


class AuthenticatedResource(Resource):
    method_decorators = [jwt_required()]
