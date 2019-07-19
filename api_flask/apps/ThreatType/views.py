
from flask import Blueprint

from flask_restful import Resource, Api
import api_flask.apps.ThreatType.elastick_call as api_call


threat_type_bp = Blueprint('threatType', __name__)
api = Api(threat_type_bp)

# @api_bp.route('/sites/', methods=('GET',))
class threatType(Resource):
    def get(self):
        threats = api_call.getData()
        return threats

api.add_resource(threatType, '/threat_type')
