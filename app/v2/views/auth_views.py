from collections import namedtuple 
from flask import Blueprint, request, make_response, jsonify
from app.v2.utils.serializer import Serializer
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
        return Serializer.serialize("national_id cannot be empty", 400)

    if not password:
        return Serializer.serialize("password cannot be empty", 400)

    else:
        result = auth.login_a_user(national_id, password)
        return Serializer.serialize(result, 200)
            


@auth_route.route('/signup', methods=['POST']) 
def create_a_user_account():
    data = request.get_json()

    ### Fields
    national_id = data.get('national_id')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    othername = data.get('othername')
    email = data.get('email')
    phone = data.get('phone')
    isadmin = data.get('isadmin')
    password = data.get('password')
    passporturl = data.get('passporturl')
    
    if not national_id:
        return Serializer.serialize("national_id cannot be empty", 400)
    if not firstname:
        return Serializer.serialize("firstname cannot be empty", 400)
    if not lastname:
        return Serializer.serialize("lastname cannot be empty", 400)
    if not othername:
        return Serializer.serialize("othername cannot be empty", 400)
    if not email:
        return Serializer.serialize("email cannot be empty", 400)
    if not phone:
        return Serializer.serialize("phone cannot be empty", 400)
    if not isadmin:
        return Serializer.serialize("isadmin cannot be empty", 400)
    if not password:
        return Serializer.serialize("password cannot be empty", 400)
    if not passporturl:
        return Serializer.serialize("passporturl cannot be empty", 400)
    else:
        Params = namedtuple("Params",["national_id", "firstname", "lastname", "othername", "email", "phone", "isadmin", "password", "passporturl"])
        params = Params(national_id, firstname, lastname, othername, email, phone, isadmin, password, passporturl)
        result = auth.create_a_user_account(params)
        return make_response(jsonify({'status': 201, 'data': result}), 201)

@auth_route.route('/reset/', methods=['POST']) 
def password_reset():
    data = request.get_json()
    ### Fields
    email = data.get('email')
    national_id = data.get('national_id')
    password = data.get('password')
    if not email:
        return Serializer.serialize("email cannot be empty", 400)
    if not national_id:
        return Serializer.serialize("national_id cannot be empty", 400)
    if not password:
        return Serializer.serialize("password cannot be empty", 400)
    else:
        result = auth.reset_password(national_id, email, password)
        return make_response(jsonify({'status': 200, 'data': result}), 200)