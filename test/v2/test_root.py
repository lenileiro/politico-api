import json
from .base_test import BaseTest

class TestPostRequest(BaseTest): 
    def test_vote_cast(self):
        response = self.client.post(
            "/api/v2/votes/", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["office"], int)
        self.assertIsInstance(result["data"]["voter"], int)
        self.assertIsInstance(result["data"]["candidate"], int)
    
    def test_petition(self):
        response = self.client.post(
            "/api/v2/petitions/", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["id"], int)
        self.assertIsInstance(result["data"]["office"], int)
        self.assertIsInstance(result["data"]["voter"], int)
        self.assertIsInstance(result["data"]["text"], str)
        self.assertIsInstance(result["data"]["evidence"], str)


