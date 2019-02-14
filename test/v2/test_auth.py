import json
from .base_test import BaseTest

class TestPostRequest(BaseTest): 
    def test_user_login(self):
        user = {
            "national_id": 32308961,
            "password":"123"
        }
        response = self.client.post(
            "/api/v2/auth/login",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["token"], str)
        self.assertIsInstance(result["data"]["user"], dict)
        self.assertIsInstance(result["data"]["user"]["id"], int)
        self.assertIsInstance(result["data"]["user"]["firstname"], str)
        self.assertIsInstance(result["data"]["user"]["lastname"], str)
        self.assertIsInstance(result["data"]["user"]["othername"], str)
        self.assertIsInstance(result["data"]["user"]["email"], str)
        self.assertIsInstance(result["data"]["user"]["phoneNumber"], str)
        self.assertIsInstance(result["data"]["user"]["passportUrl"], str)
        self.assertIsInstance(result["data"]["user"]["isAdmin"], str)
    
    def test_user_login_no_password(self):
        user = {
            "national_id": 32308961
        }
        response = self.client.post(
            "/api/v2/auth/login",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], "password cannot be empty")
        self.assertIsInstance(result["message"], str)
