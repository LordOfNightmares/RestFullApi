from flask import jsonify

from methods.Resource import AuthenticatedResource
from sql.DatabaseModel import DatabaseMethods
from sql.Databases import Organisation

class OrganisationHTTP(AuthenticatedResource):
    def __init__(self):
        self.file = open("file.txt", 'a')
        self.OrgDB = DatabaseMethods(Organisation)


    def post(self):
        # implement the json content type input
        self.OrgDB.__add__("Onee", "Twoe", "Threee")

    def put(self):
        # implement the json content type input
        self.OrgDB.__update__(1, "Onee", "Twoe", "Threee")

    def delete(self):
        self.OrgDB.__delete__(13)

    def get(self):
        return jsonify(self.OrgDB.__all__())
        # implement page
        # self.OrgDB.__get__(40)

# organisation = [
#     {'id': 0,
#      'name': 'O1',
#      'description': 'salary',
#      'amount': 5000}
# ]

#
# class Repository(object):
#     def __init__(self):
#         self.repos = {}
#
#     def add(self, repo):
#         self.repos[repo.get_id()] = repo
#
#     def get_id(self):
#         return self.id
#
#     def all(self):
#         return self.repos
#
#     def get(self, id):
#         return self.repos[id]
#
#     def __str__(self):
#         # _dict = dict(self)
#         # return "{" + ",\n ".join('{}:\'{}\''.format(k, _dict[k]) for k in _dict.keys()) + "}"
#         import json
#         return json.dump(dict(self))
#
#
# class Organisation(object):
#     def __init__(self, name, description):
#         self.id = 0
#         self.name = name
#         self.description = description
#
#     def __repr__(self):
#         return "<User(id='{}', name='{}', description='{}')>" % (self.id, self.name, self.description)
