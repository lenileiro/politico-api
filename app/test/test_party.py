""" Test for Admin endpoints """

import json
from .basetest import BaseTest

class TestDeleteRequest(BaseTest):

    def test_valid_delete_request(self):
        response = self.valid_delete_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(result["status"], 204)
        self.assertEqual(result["data"][0]["message"], "delete successful")
    
    def test_invalid_delete_request(self):
        response = self.invalid_delete_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "Id not found")

class TestPatchRequest(BaseTest):

    def test_valid_delete_request(self):
        response = self.valid_patch_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(result["status"], 204)
        self.assertEqual(result["data"][0]["name"], "new political party name")
    
    def test_invalid_delete_request(self):
        response = self.invalid_delete_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "Id not found")
