import psycopg2
from datetime import datetime
import os


def conn():
    DATABASE_URI = os.getenv('DATABASE_URL')
    con = psycopg2.connect(DATABASE_URI)
    return con

def init_db(url):
    DATABASE_URI = os.getenv('DATABASE_URL')
    con = psycopg2.connect(DATABASE_URI)
    cur = con.cursor()


    schema = """
            CREATE SCHEMA IF NOT EXISTS politico;
    """

    user = """
            CREATE TABLE IF NOT EXISTS politico.user (
                id SERIAL PRIMARY KEY NOT NULL,
                national_id INTEGER NOT NULL, 
                firstname VARCHAR (100) NOT NULL, 
                lastname VARCHAR (100) NOT NULL, 
                othername VARCHAR (100), 
                email VARCHAR (100) NOT NULL, 
                phone VARCHAR (100) NOT NULL, 
                isadmin VARCHAR (6) NOT NULL, 
                password VARCHAR (250) NOT NULL, 
                passporturl VARCHAR (100) NOT NULL, 
                created_at TIMESTAMP);
            """

    cur.execute(schema)
    con.commit()

    cur.execute(user)
    con.commit()

def destoy_db():
    """Delete database"""
    schema = """DROP SCHEMA IF EXISTS politico CASCADE;"""
    con = conn()
    cur = con.cursor()
    cur.execute(schema)
    con.commit()
    