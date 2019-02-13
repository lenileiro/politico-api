"""Database connection module"""
import psycopg2

class DB:
    """Database connection class"""
    def __init__(self):
        self.conn = ''
        self.cur = ''

    def connect_to(self, url):
        """connect to database"""
        self.conn = psycopg2.connect(url)
        self.cur = self.conn.cursor()

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