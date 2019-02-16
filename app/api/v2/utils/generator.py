import os
import jwt

def generate_jwt_token(payload):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, './utils/keys/jwt-key')
        secret_key = open(filename).read()
        token = jwt.encode(payload, secret_key, algorithm='HS256').decode('utf-8')
        return token