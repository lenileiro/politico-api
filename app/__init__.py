"""Main Application Logic """
from flask import Flask, render_template, jsonify, make_response
from flask_cors import CORS

from instance import config


def create_app(config_name):
    '''Function to create a flask app depending on the configuration passed'''

    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config.app_config[config_name])
    app.url_map.strict_slashes = False

    with app.app_context():
        from app.v1.views import party, office
        app.register_blueprint(party.bp)
        app.register_blueprint(office.bp)

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
