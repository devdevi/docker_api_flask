
from flask import Blueprint

from flask_restful import Resource, Api
import api_flask.apps.UserAgent.elastick_call as api_call


user_agent_bp = Blueprint('UserAgent', __name__)
api = Api(user_agent_bp)

class UserAgent(Resource):
    def get(self):
        data = api_call.getData()
        return data

api.add_resource(UserAgent, '/user_agent')
