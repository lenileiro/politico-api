import json
from .base import BaseTest


class TestPostRequest(BaseTest):

    def test_valid_post_request(self):
        create_office = {
            "type": 'national',
            "name": "President"
        }
        response = self.client.post(
            '/api/v1/offices', data=json.dumps(create_office),
            content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"][0]["type"], "national")
        self.assertEqual(result["data"][0]["name"], "President")

    def test_invalid_post_request_1(self):
        create_office = {
            "type": 'national'
        }
        response = self.client.post(
            '/api/v1/offices', data=json.dumps(create_office),
            content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], "Name cannot be empty")

    def test_invalid_post_request_2(self):
        create_office = {
            "name": "President"
        }
        response = self.client.post(
            '/api/v1/offices', data=json.dumps(create_office),
            content_type="application/json")
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

    def test_individual_get_request_not_found(self):
        response = self.client.get(
            "/api/v1/offices/10000320", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["status"], 404)
        self.assertEqual(result["message"], "Office Id not found")
