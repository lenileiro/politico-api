import unittest
import instance
from DB.createdb import main, connect_to_db
from app import create_app

class BaseTest(unittest.TestCase):
    """ Test class for user endpoints """

    def setUp(self):
        main('testing')
        self.app = create_app('testing')
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