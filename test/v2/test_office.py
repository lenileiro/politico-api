import json
from .base_test import BaseTest

class TestGetRequest(BaseTest): 
    def test_fetch_all_office(self):
        response = self.client.get(
            "/api/v2/offices", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], list)
        self.assertIsInstance(result["data"][0], dict)
        self.assertIsInstance(result["data"][0]["id"], int)
        self.assertIsInstance(result["data"][0]["type"], str)
        self.assertIsInstance(result["data"][0]["office"], str)

    def test_fetch_specific_office(self):
        response = self.client.get(
            "/api/v2/parties/1", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["id"], int)
        self.assertIsInstance(result["data"]["type"], str)
        self.assertIsInstance(result["data"]["name"], str)

    def test_fetch_specific_office_results(self):
        response = self.client.get(
            "/api/v2/office/1/result", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], list)
        self.assertIsInstance(result["data"][0], dict)
        self.assertIsInstance(result["data"][0]["office"], int)
        self.assertIsInstance(result["data"][0]["candidate"], int)
        self.assertIsInstance(result["data"][0]["result"], int)

class TestPostRequest(BaseTest): 
    def test_create_office(self):
        response = self.client.post(
            "/api/v2/parties", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["id"], int)
        self.assertIsInstance(result["data"]["type"], str)
        self.assertIsInstance(result["data"]["name"], str)

    def test_register_citizen_as_candidate(self):
        response = self.client.post(
            "/api/v2/office/1/register", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["office"], int)
        self.assertIsInstance(result["data"]["candidate"], int)

