from collections import namedtuple 
from flask import Blueprint, request
from utils.serializer import Serializer as sp

from db.models import AuthModel, Base

auth = AuthModel()

bp = Blueprint('auth-v2', __name__, url_prefix='/api/v2/auth') 


@bp.route('/signup', methods=['POST'])
def create_account():
    data = request.get_json()

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
        return sp.error("national_id cannot be empty", 400)
    if not firstname:
        return sp.error("firstname cannot be empty", 400)
    if not lastname:
        return sp.error("lastname cannot be empty", 400)
    if not othername:
        return sp.error("othername cannot be empty", 400)
    if not email:
        return sp.error("email cannot be empty", 400)
    if not phone:
        return sp.error("phone cannot be empty", 400)
    if not isadmin:
        return sp.error("isadmin cannot be empty", 400)
    if not password:
        return sp.error("password cannot be empty", 400)
    if not passporturl:
        return sp.error("passporturl cannot be empty", 400)
    else:
        userfound = '{}'.format(auth.get("user", national_id=national_id))

        if userfound != "None":
            return sp.error("User exits in Database", 404)

        else:
            Params = namedtuple("Params", ["national_id", "firstname", "lastname", "othername", "email", "phone", "isadmin", "password", "passporturl"])
            params = Params(national_id, firstname, lastname, othername, email, phone, isadmin, password, passporturl)
            response = auth.insert_user(params)
            return sp.sdict(response, 201)

@bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    national_id = data.get('national_id')
    password = data.get('password')

    if not national_id:
        return sp.error("national_id cannot be empty", 400)
    if not password:
        return sp.error("password cannot be empty", 400)

    else:

        userfound = '{}'.format(auth.get("user", national_id=national_id))
        if userfound != "None":
            response = auth.login_user(national_id, password)
            
            return sp.sdict(response)

        else:
             return sp.error("User is not registered", 404)

        

@bp.route('/reset/', methods=['POST'])
def reset_password():
    pass
