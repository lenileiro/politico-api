from flask import Flask, make_response, jsonify
from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    from .api.v1.views import party_views, office_views
    app.register_blueprint(party_views.parties_route)
    app.register_blueprint(office_views.office_route)
    
    return app
    