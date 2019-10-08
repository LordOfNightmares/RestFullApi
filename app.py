from flask import Blueprint
from flask_restful import Api
from flask_jwt import JWT, jwt_required, current_identity
from config import config, userid_table, username_table, Auth
from flask import Flask

app = Flask(__name__)
config(app)
# blueprint api
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
app.register_blueprint(api_bp, url_prefix='/api')
# Authentication
auth = Auth(username_table, userid_table)
jwt = JWT(app, auth.authenticate, auth.identity)

# Routes

from HelloWorld import Hello

api.add_resource(Hello, '/Hello')
