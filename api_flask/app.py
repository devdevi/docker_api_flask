from flask import Flask, Blueprint
from flask_restful import Api
from api_flask.apps.Hello import Hello

api_bp_hello = Blueprint('api', __name__)
api = Api(api_bp_hello)

# Route
api.add_resource(Hello, '/')

def create_app():
    app = Flask(__name__)
    # app.config.from_object(config_filename)
    from api_flask.apps.Activity.views import activity_bp
    app.register_blueprint(activity_bp, url_prefix='/api/v1')

    from api_flask.apps.Attack.views import attack_bp
    app.register_blueprint(attack_bp, url_prefix='/api/v1')

    from api_flask.apps.AttackCode.views import attack_code_bp
    app.register_blueprint(attack_code_bp, url_prefix='/api/v1')

    from api_flask.apps.ThreatType.views import threat_type_bp
    app.register_blueprint(threat_type_bp, url_prefix='/api/v1')

    from api_flask.apps.ServerResponse.views import server_response_bp
    app.register_blueprint(server_response_bp, url_prefix='/api/v1')

    from api_flask.apps.UserAgent.views import user_agent_bp
    app.register_blueprint(user_agent_bp, url_prefix='/api/v1')

    app.register_blueprint(api_bp_hello)
    return app
