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

    def request_data(self):
        if request.get_json():
            data = request.get_json()
        else:
            data = request.form.to_dict()
        return data

    def post(self, *args, **kwargs):
        data = self.request_data()
        if 'id' in data and self.OrgDB.__get__(data['id']):
            del data['id']
        self.content = str(self.OrgDB.__add__(**data))
        return make_response(self.content)

    def patch(self, *args, **kwargs):
        data = self.request_data()
        self.content = str(self.OrgDB.__update__(**data))
        return make_response(self.content)

    def delete(self, *args, **kwargs):
        if 'id' in self.request_data():
            self.content = str(self.OrgDB.__delete__(self.request_data()['id']))
            return make_response(self.content)
        return jsonify("Please input id.")

    def get(self, *args, **kwargs):
        self.content = self.OrgDB.__all__()
        return make_response(str(self.content))


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
        data = self.request_data()
        data.update({'id': id})
        self.content = str(self.OrgDB.__update__(**data))
        return make_response(self.content)

    def get(self, id):
        self.content = str(self.OrgDB.__get__(id))
        return make_response(self.content)
