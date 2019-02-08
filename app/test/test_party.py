""" Test for party endpoints """

import json
from .basetest import BaseTest


class TestDeleteRequest(BaseTest):    
    def test_invalid_delete_request(self):
        response = self.invalid_delete_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "Id not found")
    
    def test_valid_delete_request(self):
        response = self.valid_delete_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["data"][0]["message"], "delete successful")


class TestPatchRequest(BaseTest):    
    def test_invalid_delete_request(self):
        response = self.invalid_patch_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "Id not found")

    def test_valid_patch_request(self):
        response = self.valid_patch_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["data"][0]["name"], "new political party name")

class TestPostRequest(BaseTest):    
    def test_valid_post_request(self):
        response = self.valid_post_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"][0]["name"], "party C")

    def test_invalid_post_request_1(self):
        response = self.invalid_post_request_1()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "some required fields missing")
    
    def test_invalid_post_request_2(self):
        response = self.invalid_post_request_2()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "some required fields missing")
    
    def test_invalid_post_request_3(self):
        response = self.invalid_post_request_3()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "some required fields missing")