
from flask import Blueprint

from flask_restful import Resource, Api
import api_flask.apps.ServerResponse.elastick_call as api_call

server_response_bp = Blueprint('serverResponse', __name__)
api = Api(server_response_bp)

class ServerResponse(Resource):
    def get(self):
        # print(api_call.activitySitesData())
        serverResponse = api_call.serverResponse()
        return serverResponse

api.add_resource(ServerResponse, '/server_response')