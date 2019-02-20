import os
from psycopg2 import connect
from datetime import datetime
from flask import current_app

def connect_to_db(config=None):
    db_name = current_app.config.get('DATABASE_URI')
    return connect(db_name)

def create_users_table(cur):
    cur.execute("""
        CREATE SCHEMA IF NOT EXISTS politico;
        """)
    cur.execute(
        """CREATE TABLE IF NOT EXISTS politico.user (
            id SERIAL NOT NULL,
            national_id int NOT NULL PRIMARY KEY , 
            firstname VARCHAR (100) NOT NULL, 
            lastname VARCHAR (100) NOT NULL, 
            othername VARCHAR (100), 
            email VARCHAR (100) NOT NULL, 
            phone VARCHAR (100) NOT NULL, 
            isadmin VARCHAR (6) NOT NULL, 
            password VARCHAR (250) NOT NULL, 
            passporturl VARCHAR (100) NOT NULL, 
            created_at TIMESTAMP);""")

def create_reset_password_table(cur):
    cur.execute(
        """CREATE TABLE IF NOT EXISTS politico.pass(
            id SERIAL PRIMARY KEY NOT NULL,
            passkey VARCHAR (255) NOT NULL,
            national_id INTEGER NOT NULL,
            FOREIGN KEY (national_id) REFERENCES politico.user (national_id));"""
    )

    
def init_db(config=None):

    conn = connect_to_db(config=config)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    create_users_table(cur)
    create_reset_password_table(cur)

    cur.close()
    conn.commit()
    conn.close()
    print('Database created successfully')


if __name__ == '__main__':
    init_db()
    