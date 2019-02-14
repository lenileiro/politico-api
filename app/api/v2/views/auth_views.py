from flask import Blueprint, request, make_response, jsonify
from ..models.auth_model import AuthModel

auth = AuthModel()
auth_route = Blueprint('auth-v2', __name__, url_prefix='/api/v2/auth') 

@auth_route.route('/login', methods=['POST'])
def login_user_account():
    data = request.get_json()

    ### Fields
    email = data.get('email')
    password = data.get('password')

    if not email:
        return make_response(jsonify({
            "status": 400,
            "message": "email cannot be empty"
        })), 400
    if not password:
        return make_response(jsonify({
            "status": 400,
            "message": "password cannot be empty"
        })), 400

    else:
        results = auth.login_user(email, password)
       
            
        return make_response(jsonify({"status": 201,
                                      "data": results })), 201
 