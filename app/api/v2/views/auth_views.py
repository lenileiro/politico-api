from flask import Blueprint, request, make_response, jsonify
from ..models.auth_models import AuthModel

auth = AuthModel()

auth_route = Blueprint('auth-v2', __name__, url_prefix='/api/v2/auth') 

@auth_route.route('/login', methods=['POST']) 
def login_a_user():
    data = request.get_json()

    ### Fields
    national_id = data.get('national_id')
    password = data.get('password')

    if not national_id:
        return make_response(jsonify({
            "status": 400,
            "message": "national_id cannot be empty"
        })), 400
        
    if not password:
        return make_response(jsonify({
            "status": 400,
            "message": "password cannot be empty"
        })), 400

    else:
        result = auth.login_a_user(national_id, password)
            
        return make_response(jsonify({"status": 200, 
        "data": result})), 200