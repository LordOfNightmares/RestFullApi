from flask import request, make_response, jsonify

# from flask_restful import Resource
from methods.Authentication import AuthenticatedResource
from sql.DatabaseModel import DatabaseMethods
from sql.Databases import Organisation


class OrganisationHTTP(AuthenticatedResource):
    def __init__(self):
        self.OrgDB = DatabaseMethods(Organisation)
        self.page = open('org.html', 'r').read().replace('\n', '')

    def rsp(self):
        return make_response("<br>".join('{}'.format(k) for k in [self.page, self.content, self.current()]))

    def current(self):
        return str(self.OrgDB.__all__())

    def post(self):
        name = request.form['Name']
        desc = request.form['Description']
        pos = request.form['Position']
        self.content = str(self.OrgDB.__add__(name, desc, pos))
        return self.rsp()

    def put(self):
        self.content = str(self.OrgDB.__update__(**request.get_json()))
        return self.rsp()

    def delete(self, id):
        # id = request.args
        self.content = str(self.OrgDB.__delete__(id))
        return self.rsp()

    def get(self):
        self.content = str(self.OrgDB.__all__())
        return make_response("<br>".join('{}'.format(k) for k in [self.page, self.content]))


class Organisation1(OrganisationHTTP):
    def __init__(self):
        super().__init__()

    def delete(self):
        return jsonify("Please input id.")


class Organisation2(OrganisationHTTP):
    def __init__(self):
        super().__init__()
