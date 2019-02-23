import re
from collections import namedtuple
from flask import Blueprint, request
from utils.serializer import Serializer as sp
from flask_restful import reqparse
from utils.validations import Validator as vl
from utils.helper import Auth 
from utils.tokens import Token

from ..models.auth import AuthModel

auth = AuthModel()

bp = Blueprint('party-v2', __name__, url_prefix='/api/v2/parties')


@bp.route('', methods=['GET'])
def fetch_all_parties():
    t = Auth.get_auth()
    d = Token.decode_token(t)
    return sp.sdict(d)

@bp.route('/1', methods=['GET'])
def fetch_a_party():
    return sp.error("one party found")

