""" Test for Admin endpoints """
from .basetest import BaseTest
import json
class TestSignup(BaseTest):

    def test_valid_delete_request(self):
        response = self.valid_delete_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["data"][0]["message"], "delete successful")
    
    def test_invalid_delete_request(self):
        response = self.invalid_delete_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "Id not found")
