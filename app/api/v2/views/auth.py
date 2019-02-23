import re
from collections import namedtuple
from flask import Blueprint, request
from utils.serializer import Serializer as sp
from flask_restful import reqparse
from utils.validations import Validator as vl

from ..models.auth import AuthModel

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

    email_format = re.compile(
        r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)")
    url_format = re.compile(
        r"^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"
    )

    if vl.is_blank(passporturl) or vl.is_blank(password) or vl.is_blank(isadmin) or vl.is_blank(phone) or vl.is_blank(email) or vl.is_blank(firstname) or vl.is_blank(lastname) or vl.is_blank(othername) or vl.is_blank(email):
        return sp.error('All fields are required', 400)
    if not (isinstance(national_id, int)):
        return sp.error('National ID should be numbers', 400)
    elif not (re.match(email_format, email)):
        return sp.error('Invalid email. Ensure email is of the form example@mail.com', 400)
    elif not (re.match(url_format, passporturl)):
        return sp.error('Invalid passport url format', 400)
    if len(password) < 8:
        return sp.error('Password should be atleast 8 characters', 400)

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
            return sp.error("User exits in Database", 409)

        else:
            Params = namedtuple(
                "Params", ["national_id", "firstname", "lastname", "othername", "email", "phone", "isadmin", "password", "passporturl"]
                )
            params = Params(
                national_id, firstname, lastname, othername, email, phone, isadmin, password, passporturl
                )
            response = auth.insert_user(params)
            return sp.sdict(response, 201)


@bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    national_id = data.get('national_id')
    password = data.get('password')
    if vl.is_blank(password):
        return sp.error('password fields is required', 400)
    if not (isinstance(national_id, int)):
        return sp.error('National ID should be numbers', 400)
    if len(password) < 8:
        return sp.error('Password should be atleast 8 characters', 400)


    if not national_id:
        return sp.error("national_id cannot be empty", 400)
    if not password:
        return sp.error("password cannot be empty", 400)

    else:

        userfound = '{}'.format(auth.get("user", national_id=national_id))
        if userfound != "None":
            response = auth.login_user(national_id, password)

            if response:
                return sp.sdict(response)
            else:
                return sp.sdict({"message": "Invalid Password"}, 400)

        else:
            return sp.error("User is not registered", 404)

        
@bp.route('/reset/key', methods=['POST'])
def reset_key():
    data = request.get_json()
    national_id = data.get('national_id')
    if not (isinstance(national_id, int)):
        return sp.error('National ID should be numbers', 400)

    if not national_id:
        return sp.error("national_id cannot be empty", 400)
    else:
        response = auth.reset_key(national_id)
        return sp.sdict(response)


@bp.route('/reset/', methods=['POST'])
def reset_password():
    data = request.get_json()
    national_id = data.get('national_id')
    passkey = data.get('passkey')
    password = data.get('password')

    if not national_id:
        return sp.error("national_id cannot be empty", 400)
        
    if len(password) < 8:
        return sp.error('Password should be atleast 8 characters', 400)

    if not national_id:
        return sp.error("national_id cannot be empty", 400)

    if not national_id:
        return sp.error("national_id cannot be empty", 400)
    if not passkey:
        return sp.error("passkey cannot be empty", 400)
    if not password:
        return sp.error("password cannot be empty", 400)
    else:
        response = auth.reset_password(national_id, passkey, password)
        if response:
            return sp.sdict(response)
        else:
            return sp.error("key Provided does not work", 401)
