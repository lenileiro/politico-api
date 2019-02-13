import json
from .base_test import BaseTest

class TestGetRequest(BaseTest):    
    def test_fetch_all_parties(self):
        response = self.client.get(
            "/api/v2/parties", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], list)
        self.assertIsInstance(result["data"][0], dict)
        self.assertIsInstance(result["data"][0]["id"], int)
        self.assertIsInstance(result["data"][0]["name"], str)



    def test_fetch_specific_party(self):
        response = self.client.get(
            "/api/v2/parties/1", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["id"], int)
        self.assertIsInstance(result["data"]["name"], str)

        
class TestDeleteRequest(BaseTest):    
    def test_delete_specific_party(self):
        response = self.client.delete(
            "/api/v2/parties/1", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["message"], str)
        self.assertEqual(result["data"]["message"], "delete successful")

class TestPostRequest(BaseTest):    
    def test_create_party(self):
        response = self.client.post(
            "/api/v2/parties", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["id"], int)
        self.assertIsInstance(result["data"]["name"], str)

class TestPatchRequest(BaseTest):    
    def test_edit_specific_party(self):
        response = self.client.patch(
            "/api/v2/parties/1", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["id"], int)
        self.assertIsInstance(result["data"]["name"], str)


