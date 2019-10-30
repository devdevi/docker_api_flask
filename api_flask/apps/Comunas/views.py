
from flask import Blueprint

from flask_restful import Resource, Api
import api_flask.apps.Comunas.api_call as api_call


comunas_bp = Blueprint('comunas', __name__)
api = Api(comunas_bp)

# @api_bp.route('/sites/', methods=('GET',))
class Comunas(Resource):
    def get(self):
        comunas = api_call.getComunas()
        return comunas

api.add_resource(Comunas, '/comunas',)


class Comuna(Resource):
    def get(self):
        comunas = api_call.getComunas()
        return comunas
api.add_resource(Comunas, '/comuna/<str:name>', endpoint='comuna_name')




