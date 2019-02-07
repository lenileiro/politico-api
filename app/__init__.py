from flask import Flask, make_response, jsonify
from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    from .api.views import party_views
    app.register_blueprint(party_views.parties_route)
    
    return app
    