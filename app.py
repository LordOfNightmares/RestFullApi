from flask import Blueprint
from flask_restful import Api
from flask_jwt import JWT, jwt_required, current_identity
from config import config, userid_table, username_table
from flask import Flask
from methods.Authentication import Auth

app = Flask(__name__)
app.config = config()
# blueprint api
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
app.register_blueprint(api_bp, url_prefix='/api')
# Authentication
auth = Auth(username_table, userid_table)
jwt = JWT(app, auth.authenticate, auth.identity)

# @app.route('/protected')
# @jwt_required
# def protected():
#     return {'{}'.format(current_identity)}
#
#
# app.route('/protected')(jwt_required()(protected()))
