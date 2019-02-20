from random import randint
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
            return "Invalid Password"
    
    @staticmethod
    def reset_key(national_id):
        cur.execute(
            """SELECT * FROM politico.pass where national_id={} """.format(national_id)
        )
        key_found = cur.fetchone()
        if key_found:
            sql = """UPDATE politico.pass SET passkey=%(passkey)s where national_id=(%(national_id)s)
                """
            passkey ='key-{}'.format(randint(101, 1000))
            cur.execute(sql, {"passkey": str(passkey), "national_id": national_id})
            return passkey

        else:
            sql = """INSERT INTO politico.pass
                (national_id, passkey) values (%(national_id)s, %(passkey)s)
                """
            passkey = 'key-{}'.format(randint(101, 1000))
            cur.execute(sql, {"passkey": str(passkey), "national_id": national_id})
            return passkey
    
    @staticmethod
    def reset_password(national_id, passkey, password):
        cur.execute(
            f"""SELECT * FROM politico.pass as cs inner join politico.user cy on cs.national_id=cy.national_id where cs.passkey='{passkey}'"""
        )
        key_found = cur.fetchall()

        if key_found:
            sql = """UPDATE politico.user SET password=%(password)s where national_id=(%(national_id)s)
                """
            cur.execute(sql, {"password": '{}'.format(generate_password_hash(password)), "national_id": national_id})

            return "password reset complete"
        
        else:
            return False

     
        