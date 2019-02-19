import json
import unittest
import instance
from app import create_app


class BaseTest(unittest.TestCase):

    def setUp(self):
        """ Defining test variables """
        self.app = create_app('testing')
        self.client = self.app.test_client()


if __name__ == "__main__":
    unittest.main()
