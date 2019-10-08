from flask_restful import Resource
from app import jwt_required


class AuthResource(Resource):
    method_decorators = [jwt_required()]


class Hello(AuthResource):
    def get(self):
        return {"message": "Hello,GET World!"}

    def post(self):
        return {"message": "Hello,POST World!"}
