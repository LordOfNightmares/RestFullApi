from methods.Authentication import *
from methods.UserModel import *

# from methods.Organization import *


users = [
    User(1, 'user1', 'aaa'),
    User(2, 'user2', 'abcxyz')
]
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def config(app):
    from datetime import timedelta
    app.debug = True
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=86400)
