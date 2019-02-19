import json
import unittest
import instance
from app import create_app
from db.createdb import connect_to_db


class BaseTest(unittest.TestCase):

    def setUp(self):
        """ Defining test variables """
        self.app = create_app('testing')
        self.app.app_context().push()
        self.client = self.app.test_client()
    
    def tearDown(self):
        conn = connect_to_db('testing')
        cur = conn.cursor()
        cur.execute("""DROP TABLE IF EXISTS politico.user CASCADE""" )
        cur.close()
        conn.commit()
        conn.close()
        
    

if __name__ == "__main__":
    unittest.main()
