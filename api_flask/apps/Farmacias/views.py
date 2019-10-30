
from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api
import api_flask.apps.Farmacias.api_call as api_call

farmacia_bp = Blueprint('farmacias', __name__)
api = Api(farmacia_bp)

class Farmacias(Resource):
    def get(self):
        farmacias = api_call.getFarmacias()
        return farmacias

api.add_resource(Farmacias, '/farmacias')

class Query(Resource):
    def get(self, comuna_name, farmacia_name):
        result = api_call.filterComuna(comuna_name, farmacia_name)
        return jsonify(result)
api.add_resource(Query, '/comuna/<comuna_name>/farmacia/<farmacia_name>')  # Route_3