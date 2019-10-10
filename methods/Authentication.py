from flask_jwt import jwt_required
from flask_restful import Resource


class AuthenticatedResource(Resource):
    method_decorators = [jwt_required()]


class ConnectionAuth:
    def __init__(self, username_table, userid_table):
        self.username_table = username_table
        self.userid_table = userid_table

    def authenticate(self, username, password):
        print(username)
        from werkzeug.security import safe_str_cmp
        user = self.username_table.get(username, None)
        if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user

    def identity(self, payload):
        user_id = payload['identity']
        return self.userid_table.get(user_id, None)
