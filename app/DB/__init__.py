"""Database connection module"""
import psycopg2

class DB:
    """Database connection class"""

    @classmethod
    def connect_to(cls, url):
        cls.conn = psycopg2.connect(url)

    @classmethod
    def send_con(cls):
        cls.cursor = cls.conn.cursor()
        return cls.conn
    
    
    @classmethod
    def init_db(cls):
        """create database tables"""
        schema = """
        CREATE SCHEMA IF NOT EXISTS politico
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
        con = cls.send_con()
        cur = con.cursor()
        cur.execute(schema)
        con.commit()
        cur.execute(user)
        con.commit()

    @classmethod
    def destoy_db(cls):
        """Delete database"""
        schema = """
         DROP SCHEMA IF EXISTS politico CASCADE;
        """
        con = cls.send_con()
        cur = con.cursor()
        cur.execute(schema)
        con.commit()
