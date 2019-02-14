from flask import Flask, make_response, jsonify, render_template
from instance.config import app_config
from app.DB.tables import init_db

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    
    from .api.v1.views import party_views, office_views
    app.register_blueprint(party_views.parties_route)
    app.register_blueprint(office_views.office_route)

    from .api.v2.views import auth_views
    app.register_blueprint(auth_views.auth_route)

    @app.route("/")
    def index():
        return render_template("api-docs.html")

    @app.errorhandler(404)
    def resource_not_found(message):
        """ Handling resource not found """

        return make_response(jsonify({
            "status": 404,
            "message": str(message)
        })), 404

    @app.errorhandler(405)
    def method_not_allowed(message):
        """ Handling method not allowed error """

        return make_response(jsonify({
            "status": 405,
            "message": str(message)
        })), 405

    @app.errorhandler(500)
    def server_internal_error(message):
        """ Handling internal server error """
        return make_response(jsonify({
            "status": 500,
            "message": str(message)
        })), 500

    app.register_error_handler(404, resource_not_found)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(500, server_internal_error)

    return app
    