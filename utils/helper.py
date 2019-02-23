import os
import jwt
from functools import wraps
from flask import request
from utils.serializer import Serializer as sp
from utils.tokens import Token

class Auth:
    @staticmethod
    def get_auth():
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return sp.error("token missing", 401)
        else:
            return(authorization_header)
