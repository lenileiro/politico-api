import json
from .base import BaseTest

class TestPostRequest(BaseTest):

    def test_valid_post_request(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
            "othername": "smith",
            "email": "johndoe@gmail.com",
            "isadmin": "False",
            "phone": "+254724862149",
            "password":"123",
            "passporturl": "demo.com/image.jpg"
        }
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(user),
            content_type="application/json")
            
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], str)