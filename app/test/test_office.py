""" Test for Office endpoints """

import json
from .basetest import BaseTest

class TestPostRequest(BaseTest):    
    def test_valid_post_request(self):
        response = self.valid_office_post_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"][0]["type"], "national")
        self.assertEqual(result["data"][0]["name"], "President")

    def test_invalid_post_request_1(self):
        response = self.invalid_office_post_request_1()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "some required fields missing")


class TestGetRequest(BaseTest):    
    def test_valid_get_request(self):
        response = self.valid_get_request()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
