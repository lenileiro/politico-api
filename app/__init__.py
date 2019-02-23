from flask import Flask, make_response, jsonify, render_template
from instance.config import app_config
from db.createdb import init_db

from flask import current_app


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.app_context().push()
    #print(app.config['DATABASE_URI'])
    init_db(app.config['DATABASE_URI'])

    from .api.v1.views import party, office
    app.register_blueprint(party.bp)
    app.register_blueprint(office.bp)

    from .api.v2.views import auth , party
    app.register_blueprint(auth.bp)
    app.register_blueprint(party.bp)

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
    
