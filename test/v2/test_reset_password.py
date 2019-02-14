import json
from .base_test import BaseTest

class TestPostRequest(BaseTest): 
    def test_user_login(self):
        user = {
            "email": "johndoe@gmail.com"
        }
        response = self.client.post(
            "/api/v2/auth/reset/",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["message"], str)
        self.assertIsInstance(result["data"]["email"], str)
