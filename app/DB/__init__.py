"""Database connection module"""
import psycopg2
from flask import current_app


class DB:
    """Database connection class"""
    def __init__(self):
        self.conn = ''
        self.cur = ''

    def connect_to(self, url):
        """connect to database"""
        self.conn = psycopg2.connect(url)
        self.cur = self.conn.cursor()
    
    def create_tables(self):
        try:
            user = """
            CREATE TABLE IF NOT EXISTS user (
                u_id SERIAL PRIMARY KEY NOT NULL, 
                firstname VARCHAR (100) NOT NULL, 
                lastname VARCHAR (100) NOT NULL, 
                othername VARCHAR (100), 
                username VARCHAR (100) NOT NULL, 
                email VARCHAR (100) NOT NULL, 
                phone VARCHAR (100) NOT NULL, 
                isAdmin BOOLEAN, 
                u_password VARCHAR (250) NOT NULL, 
                created_at TIMESTAMP);
            """
            party = """
            CREATE TABLE IF NOT EXISTS party (
                p_id SERIAL PRIMARY KEY NOT NULL, 
                p_name VARCHAR (100) NOT NULL, 
                hqAddress VARCHAR (100) NOT NULL, 
                logoUrl VARCHAR (100) NOT NULL);
            """

            office ="""
            CREATE TABLE IF NOT EXISTS office (
                o_id SERIAL PRIMARY KEY NOT NULL, 
                o_name VARCHAR (100) NOT NULL, 
                o_type VARCHAR (100) NOT NULL);
            """
            candidate = """
            CREATE TABLE IF NOT EXISTS candidates (
                c_id SERIAL PRIMARY KEY NOT NULL, 
                c_office INTEGER REFERENCES office(o_id), 
                c_party INTEGER REFERENCES party(p_id), 
                c_candidate INTEGER REFERENCES user(u_id));
            """
            vote = """
            CREATE TABLE IF NOT EXISTS vote (
                c_id SERIAL PRIMARY KEY NOT NULL, 
                createdOn DATE NOT NULL, 
                createdBy INTEGER REFERENCES user(u_id), 
                office INTEGER REFERENCES office(o_id), 
                c_candidate INTEGER REFERENCES candidates(c_id));
            """
            petition = """
            CREATE TABLE IF NOT EXISTS petition (
                p_id SERIAL PRIMARY KEY NOT NULL, 
                createdOn DATE NOT NULL, 
                createdBy INTEGER REFERENCES user(u_id), 
                office INTEGER REFERENCES office(o_id), 
                body VARCHAR (256) NOT NULL);
            """

            tables = [user, party, office, candidate, vote, petition]
            for table in tables:
                self.save_incoming_data_or_updates(table)
                
        except Exception as e:
            print("Database exception: %s" % e)

    def fetch_single_data_row(self, query):
        """ retreives a single row of data from a table """
        self.cur.execute(query)
        fetchedRow = self.cur.fetchone()
        return fetchedRow

    def save_incoming_data_or_updates(self, query):
        """ saves data passed as a query to the stated table """
        self.cur.execute(query)
        self.conn.commit()

    def fetch_all_tables_rows(self, query):
        """ fetches all rows of data store """
        self.cur.execute(query)
        all_data_rows = self.cur.fetchall()
        return all_data_rows