
from flask import Blueprint

from flask_restful import Resource, Api
import api_flask.apps.AttackCode.elastick_call as api_call


attack_code_bp = Blueprint('AttackCode', __name__)
api = Api(attack_code_bp)

# @api_bp.route('/sites/', methods=('GET',))
class AttackCode(Resource):
    def get(self):
        # print(api_call.AttackCodeSitesData())
        sites = api_call.getData()
        return sites

api.add_resource(AttackCode, '/attack_code')
