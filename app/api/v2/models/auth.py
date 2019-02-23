from datetime import datetime
from random import randint
from werkzeug.security import generate_password_hash, check_password_hash
from db import models, createdb
from utils.tokens import Token
from flask import current_app

conn = createdb.connect_to_db(current_app.config.get('DATABASE_URI'))
conn.set_session(autocommit=True)
cur = conn.cursor()


class AuthModel(models.Base):

    @staticmethod
    def insert_user(params):
        created_at = '%s' % (datetime.now().strftime("%Y-%m-%d"))
        user = {
            "national_id": params.national_id,
            "firstname": params.firstname,
            "lastname": params.lastname,
            "othername": params.othername,
            "email": params.email,
            "isadmin": params.isadmin,
            "phone": params.phone,
            "password": generate_password_hash(params.password),
            "passporturl": params.passporturl,
            "created_at": created_at
        }
        models.Base.insert('user', user)

        token = Token.generate_token(
            national_id=params.national_id,
            isadmin=params.isadmin)

        response = {
                    "token": token,
                    "user": {
                        "national_id": params.national_id,
                        "firstname": params.firstname,
                        "lastname": params.lastname,
                        "othername": params.othername,
                        "email": params.email,
                        "isadmin": params.isadmin,
                        "phone": params.phone,
                        "passporturl": params.passporturl
                    }
                }

        return response

    @staticmethod
    def login_user(national_id, password):
        user = models.Base.get('user', national_id=national_id)
        token = Token.generate_token(national_id=national_id, isadmin=user[7])

        data = {"token": token,
                "user":
                    {
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
            return False

    @staticmethod
    def reset_key(national_id):
        key_found = models.Base.get(
            'pass', national_id=national_id)
        if key_found:
            passkey = 'key-{}'.format(randint(101, 1000))

            models.Base.update(
                'pass', national_id, national_id, passkey=passkey)
            return passkey

        else:
            passkey = 'key-{}'.format(randint(101, 1000))
            data = {
                "national_id": national_id,
                "passkey": passkey
            }

            models.Base.insert(
                'pass', data)
            return passkey

    @staticmethod
    def reset_password(national_id, passkey, password):
        key_found = models.Base.joinInner(
            'pass', 'user', "national_id", passkey=passkey)
        if key_found:
            pwd = generate_password_hash(password)
            models.Base.update('user', national_id, national_id, password=pwd)
            
            passkey = 'key-{}'.format(randint(101, 1000))
            models.Base.update(
                'pass', national_id, national_id, passkey=passkey)
            return "password reset complete"
        else:
            return False
