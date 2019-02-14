import os
import jwt
from app.DB.tables import conn
from werkzeug.security import generate_password_hash, check_password_hash

class AuthModel:
    def __init__(self):
        self.db = conn()

    def login_a_user(self, national_id, password):
        cursor = self.db.cursor()
        cursor.execute(
            """SELECT * FROM politico.user where national_id={} """.format(national_id)
        )
        user = cursor.fetchone()

        if user:
            ### User not empty 
            token = self.generate_jwt_token({"id":national_id})
            strinfied = "{}".format(token)

            data = {
                "token": strinfied,
                "user": {
                "id": user[1],
                "firstname": user[2],
                "lastname": user[3],
                "othername": user[4],
                "email": user[5],
                "phoneNumber": user[6],
                "passportUrl": user[9],
                "isAdmin": user[7]
                }
            }

            stored_passord = user[8]
            results = check_password_hash(stored_passord, password)

            if results:
                return data
            else:
                return {
                "message": "Invalid Password"
            }
        else:
            return {
                "message": "User not registered"
            }

        cursor.close()
    
    def generate_jwt_token(self, payload):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, './utils/keys/jwt-key')
        secret_key = open(filename).read()
        token = jwt.encode(payload, secret_key, algorithm='HS256').decode('utf-8')
        return token