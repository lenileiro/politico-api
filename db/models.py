from flask import current_app
from .createdb import connect_to_db
from datetime import datetime


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
            "password": params.password,
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

        return "user created"

    