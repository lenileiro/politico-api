""" Test for Office endpoints """

import json
from .base_test import BaseTest 
from utils.v1.dummy_office import create_office_1, create_office_2, create_office_3
class TestPostRequest(BaseTest):    
    def test_valid_post_request(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(create_office_1), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"][0]["type"], "national")
        self.assertEqual(result["data"][0]["name"], "President")

    def test_invalid_post_request_1(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(create_office_2), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], "Name cannot be empty")
    
    def test_invalid_post_request_2(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(create_office_3), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], "type cannot be empty")


class TestGetRequest(BaseTest):    
    def test_valid_get_request(self):
        response = self.client.get(
            "/api/v1/offices", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
    

    def test_valid_individual_get_request(self):
        response = self.client.get(
            "/api/v1/offices/1", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["data"][0]["id"], 1)
        