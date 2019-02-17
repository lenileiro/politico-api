from psycopg2 import connect
from flask import current_app
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

from .createdb import connect_to_db

conn = connect_to_db(current_app.config.get('APP_SETTINGS'))
conn.set_session(autocommit=True)
cur = conn.cursor()


class Base():

    def save(self):
        conn.commit()

    @staticmethod
    def get(table_name, **kwargs):

        for key, val in kwargs.items():
            sql = "SELECT * FROM {} WHERE {}='{}'".format(table_name, key, val)
            cur.execute(sql)
            item = cur.fetchone()
            return item

    @staticmethod
    def get_all(table_name):
        sql = 'SELECT * FROM {}'.format(table_name)
        cur.execute(sql)
        data = cur.fetchall()
        return data

    @staticmethod
    def update(table, id, data):
        
        for key, val in data.items():
            string = "{}='{}'".format(key, val)
            sql = 'UPDATE {} SET {} WHERE id={}'.format(table, string, id)
            cur.execute(sql)
            conn.commit()

    @staticmethod
    def delete(table, id):
        sql = 'DELETE FROM {} WHERE id={}'.format(table, id)
        cur.execute(sql)
        conn.commit()
