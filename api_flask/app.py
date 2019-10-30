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
    from api_flask.apps.Farmacias.views import farmacia_bp
    app.register_blueprint(farmacia_bp, url_prefix='/api/v1')

    from api_flask.apps.Comunas.views import comunas_bp
    app.register_blueprint(comunas_bp, url_prefix='/api/v1')

    app.register_blueprint(api_bp_hello)
    return app
