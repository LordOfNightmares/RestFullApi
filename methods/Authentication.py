# class Token_auth:
#     def __init__(self, file):
#         from ruamel.yaml import YAML
#         self.yaml = YAML()
#         self.file = file
#
#     def add_token(self, token="test"):
#         token = str(token)
#         try:
#             data = self.yaml.load(open(self.file))
#             if token not in data['token']:
#                 data['token'].append(token)
#         except:
#             data = {'token': [token]}
#         self.yaml.dump(data, open(self.file, 'w'))
#
#     def load_token(self, token):
#         return str(token) in self.yaml.load(open(self.file))['token']
#

class Auth:
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

