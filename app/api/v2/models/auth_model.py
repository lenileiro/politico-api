import jwt
import os
from app.DB import DB
from datetime import datetime

class AuthModel:

    def __init__(self):
        self.DB = DB.send_con()

    def login_user(self, email, password):
             
        cursor = self.DB.cursor()
        cursor.execute(
            """SELECT * FROM politico.user"""
        )
        user = cursor.fetchall()
        cursor.close()
        return user
    
    def generate_jwt_token(self, payload):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, './utils/keys/jwt-key')
        secret_key = open(filename).read()
        token = jwt.encode(payload, secret_key, algorithm='HS256').decode('utf-8')
        return token

        