from flask import current_app
from .createdb import connect_to_db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

conn = connect_to_db(current_app.config.get('DATABASE_URI'))
conn.set_session(autocommit=True)
cur = conn.cursor()

class Base():
    '''Base class to set up database'''

    def save(self):
        conn.commit()
    
    @staticmethod
    def get(table_name, **kwargs):
        for key, val in kwargs.items():
            sql = f"SELECT * FROM politico.{table_name} WHERE {key}='{val}'"
            cur.execute(sql)
            item = cur.fetchone()
            return item

    @staticmethod
    def get_all(table_name):
        sql = f'SELECT * FROM {table_name}'
        cur.execute(sql)
        data = cur.fetchall()
        return data

class AuthModel(Base):

    @staticmethod
    def insert_user(params):
        created_at = '%s' %(datetime.now().strftime("%Y-%m-%d"))
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
        sql = """
            INSERT INTO politico.user
            (national_id, firstname, lastname, othername, 
             email, phone, isadmin, password, passporturl,created_at)
            VALUES (%(national_id)s, %(firstname)s, %(lastname)s, %(othername)s, 
            %(email)s, %(phone)s, %(isadmin)s,%(password)s,%(passporturl)s, %(created_at)s)"""
        
        cur.execute(sql, user)

        response = {
                    "token": "token",
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
        cur.execute(
            """SELECT * FROM politico.user where national_id={} """.format(national_id)
        )
        user = cur.fetchone()

        data = {
                "token": "strinfied",
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

        