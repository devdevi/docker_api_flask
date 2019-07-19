
from flask import Blueprint

from flask_restful import Resource, Api
import api_flask.apps.Attack.elastick_call as api_call


attack_bp = Blueprint('Attack', __name__)
api = Api(attack_bp)

class Attack(Resource):
    def get(self):
        attack = api_call.getData()
        return attack

api.add_resource(Attack, '/attack')
