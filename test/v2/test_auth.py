import json
from .base_test import BaseTest

class TestPostRequest(BaseTest): 
    def test_create_user_account(self):
        response = self.client.post(
            "/api/v2/auth/signup", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertIsInstance(result["status"], int)
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
        self.assertIsInstance(result["data"]["user"]["isAdmin"], bool)

    def test_user_login(self):
        response = self.client.post(
            "/api/v2/auth/login", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["status"], int)
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
        self.assertIsInstance(result["data"]["user"]["isAdmin"], bool)

    def test_password_reset(self):
        response = self.client.post(
            "/api/v2/auth/reset/", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["message"], str)
        self.assertIsInstance(result["data"]["email"], str)

