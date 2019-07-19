
from flask import Blueprint

from flask_restful import Resource, Api
import api_flask.apps.Activity.elastick_call as api_call


activity_bp = Blueprint('activity', __name__)
api = Api(activity_bp)

# @api_bp.route('/sites/', methods=('GET',))
class Activity(Resource):
    def get(self):
        # print(api_call.activitySitesData())
        sites = api_call.activitySitesData()
        return sites

api.add_resource(Activity, '/activity')
