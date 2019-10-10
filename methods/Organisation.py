from flask import request, make_response, jsonify

# from flask_restful import Resource
from methods.Authentication import AuthenticatedResource
from sql.DatabaseModel import DatabaseMethods
from sql.Databases import Organisation


# needs auto args kwargs

class OrganisationHTTP(AuthenticatedResource):
    def __init__(self):
        self.OrgDB = DatabaseMethods(Organisation)
        self.content = ''

    def post(self, *args, **kwargs):
        self.content = str(self.OrgDB.__add__(**request.get_json()))
        return make_response(self.content)

    def patch(self, *args, **kwargs):
        self.content = str(self.OrgDB.__update__(**request.get_json()))
        return make_response(self.content)

    def delete(self, *args, **kwargs):
        return jsonify("Please input id.")

    def get(self, *args, **kwargs):
        self.content = str(self.OrgDB.__all__())
        return make_response(self.content)


class Organisation1(OrganisationHTTP):
    def __init__(self):
        super().__init__()


class Organisation2(OrganisationHTTP):
    def __init__(self):
        super().__init__()

    def delete(self, id):
        self.content = str(self.OrgDB.__delete__(id))
        return make_response(self.content)

    def patch(self, id):
        self.content = str(self.OrgDB.__update__(id, **request.get_json()))
        return make_response(self.content)

    def get(self, id):
        self.content = str(self.OrgDB.__delete__(id))
        return make_response(self.content)
