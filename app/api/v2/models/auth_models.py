import os
import jwt
from datetime import datetime
from app.DB.tables import conn
from werkzeug.security import generate_password_hash, check_password_hash
from app.api.v2.utils.generator import generate_jwt_token

class AuthModel:
    def __init__(self):
        self.db = conn()

    def login_a_user(self, national_id, password):
        cursor = self.db.cursor()
        cursor.execute(
            """SELECT * FROM politico.user where national_id={} """.format(national_id)
        )
        user = cursor.fetchone()
        cursor.close()

        if user:
            ### User not empty 
            token = generate_jwt_token({"id":national_id})
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


    def create_a_user_account(self, params):
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        password = generate_password_hash(params.password)
        user = {
            "national_id": params.national_id,
            "firstname": params.firstname,
            "lastname": params.lastname,
            "othername": params.othername,
            "email": params.email,
            "isadmin": params.isadmin,
            "phone": params.phone,
            "password": password,
            "passporturl": params.passporturl,
            "created_at": created_at
        }
        query = """
            INSERT INTO politico.user
            (national_id, firstname, lastname, othername, 
             email, phone, isadmin, password, passporturl,created_at)
            VALUES (%(national_id)s, %(firstname)s, %(lastname)s, %(othername)s, 
            %(email)s, %(phone)s, %(isadmin)s,%(password)s,%(passporturl)s, %(created_at)s)
            """

        cursor = self.db.cursor()
        cursor.execute(query, user)
        self.db.commit()
        token = generate_jwt_token(user)
        
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
                        "password": password,
                        "passporturl": params.passporturl
                    }
                }

                
        return response

    def reset_password(self, national_id, email, password):
        cursor = self.db.cursor()
        cursor.execute(
            """SELECT * FROM politico.user where national_id={} """.format(national_id)
        )
        user = cursor.fetchone()
        if user:
            password = generate_password_hash(password)

            cursor1 = self.db.cursor()
            query = """
                UPDATE politico.user SET password = '{}' WHERE id = '{}'
                """.format(password, user[0])
            cursor1.execute(query)

            cursor.close()
            response = {
                "message":"Check your mail for confirmation",
                "email": email
                }
            return response
        else:
            return {
                "message": "User not registered"
            }