import os
from flask import current_app
from .createdb import connect_to_db
from werkzeug.security import generate_password_hash, check_password_hash

conn = connect_to_db(current_app.config.get('DATABASE_URI'))
conn.set_session(autocommit=True)
cur = conn.cursor()


class Base:
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

    @staticmethod
    def delete(table_name, **kwargs):
        for key, val in kwargs.items():
            sql = f"DELETE * FROM politico.{table_name} WHERE {key}='{val}'"
            cur.execute(sql)
            item = cur.fetchone()
            return item

    @staticmethod
    def update(table_name, keyw='', valuew='', **kwargs):
        for key, val in kwargs.items():
            sql = f"""
            UPDATE politico.{table_name}
            SET {key}='{val}'
            where {keyw}={valuew}"""
            cur.execute(sql)

    @staticmethod
    def insert(table_name, data):
        keys = ','.join([key for key in data])
        values = str(tuple(data[key] for key in data))

        sql = "INSERT INTO politico.{} ({}) VALUES {}".format(
            table_name, keys, values)
        cur.execute(sql)

    @staticmethod
    def joinInner(table_name, compare_to_table, same_in_both, **kwargs):
        for key, val in kwargs.items():
            sql = f"""
                    SELECT * FROM politico.{table_name} as cs
                    inner join politico.{compare_to_table} cy
                    on cs.{same_in_both}=cy.{same_in_both}
                    where cs.{key}='{val}'"""
            cur.execute(sql)
            items = cur.fetchall()
            return items
