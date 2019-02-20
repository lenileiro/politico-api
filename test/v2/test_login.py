import json
from .base import BaseTest

class TestPostRequest(BaseTest):

    def test_user_login(self):
        user = {
            "national_id": 222222,
            "password":"123"
        }
        response = self.client.post(
            '/api/v2/auth/login', data=json.dumps(user),
            content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)

    def test_unregistered_user(self):
        user = {
            "national_id": 1235676890,
            "password":"123"
        }
        response = self.client.post(
            '/api/v2/auth/login', data=json.dumps(user),
            content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["status"], 404)
        self.assertEqual(result["message"], "User is not registered")
    
    def test_login_user_missing_password(self):
        user = {
            "national_id": 1235676890
        }
        response = self.client.post(
            '/api/v2/auth/login', data=json.dumps(user),
            content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], "password cannot be empty")
    
    def test_login_user_missing_national_id(self):
        user = {
            "password":"123"
        }
        response = self.client.post(
            '/api/v2/auth/login', data=json.dumps(user),
            content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], "national_id cannot be empty")
