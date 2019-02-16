import json
from .base_test import BaseTest

class TestPostRequest(BaseTest): 
    def test_password_reset(self):
        user = {
            "national_id": 44332211,
            "email": "johndoe@gmail.com",
            "password": "124"
        }
        response = self.client.post(
            "/api/v2/auth/reset/",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["status"], int)
    
    def test_user_with_no_email(self):
        user = {
            "national_id": 44332211,
            "password": "124"
        }
        response = self.client.post(
            "/api/v2/auth/reset/",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"], "email cannot be empty")
        self.assertIsInstance(result["data"], str)

    def test_user_with_no_password(self):
        user = {
            "national_id": 44332211,
            "email": "johndoe@gmail.com"
        }
        response = self.client.post(
            "/api/v2/auth/reset/",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"], "password cannot be empty")
        self.assertIsInstance(result["data"], str)
    
    def test_user_with_no_national_id(self):
        user = {
            "email": "johndoe@gmail.com",
            "password": "124"
        }
        response = self.client.post(
            "/api/v2/auth/reset/",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"], "national_id cannot be empty")
        self.assertIsInstance(result["data"], str)
