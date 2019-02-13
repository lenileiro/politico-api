import json
import unittest
import instance
from app import create_app
from app.DB import DB
database = DB()

app = create_app("testing")

class BaseTest(unittest.TestCase):
    """ Test class for user endpoints """

    def setUp(self):
        """ Defining test variables """
        app.config.from_object(instance.config.Testing)
        self.client = app.test_client()
    
        
        
if __name__ == "__main__":
    unittest.main()