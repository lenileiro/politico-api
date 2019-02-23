import json
from .base import BaseTest

class TestPostRequest(BaseTest):

    def test_account_creation(self):
        user = {
                "national_id": 32308961,
                "firstname": "john",
                "lastname": "Joe",
                "othername": "smith",
                "email": "johndoe@gmail.com",
                "isadmin": "False",
                "phone": "+254724862149",
                "password":"123456789",
                "passporturl": "https://demo.com/image.jpg"
            }
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(user),
            content_type="application/json")
            
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["token"], str)
        self.assertIsInstance(result["data"]["user"], dict)
        self.assertIsInstance(result["data"]["user"]["national_id"], int)
        self.assertIsInstance(result["data"]["user"]["firstname"], str)
        self.assertIsInstance(result["data"]["user"]["lastname"], str)
        self.assertIsInstance(result["data"]["user"]["othername"], str)
        self.assertIsInstance(result["data"]["user"]["email"], str)
        self.assertIsInstance(result["data"]["user"]["phone"], str)
        self.assertIsInstance(result["data"]["user"]["passporturl"], str)
        self.assertIsInstance(result["data"]["user"]["isadmin"], str)
    
    def test_account_exists(self):
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
        self.client.post(
            '/api/v2/auth/signup', data=json.dumps(user),
            content_type="application/json")
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
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["message"], str)
        self.assertEqual(result["message"], "User exits in Database")

    def test_account_creation_missing_national_id(self):
        user = {
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
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["message"], str)
        self.assertEqual(result['message'],"national_id cannot be empty")

    def test_account_creation_missing_firstname(self):
        user = {
            "national_id": 32308961,
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
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["message"], str)
        self.assertEqual(result['message'],"firstname cannot be empty")

    def test_account_creation_missing_lastname(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
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
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["message"], str)
        self.assertEqual(result['message'],"lastname cannot be empty")

    def test_account_creation_missing_othername(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
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
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["message"], str)
        self.assertEqual(result['message'],"othername cannot be empty")

    def test_account_creation_missing_email(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
            "othername": "smith",
            "isadmin": "False",
            "phone": "+254724862149",
            "password":"123",
            "passporturl": "demo.com/image.jpg"
        }
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(user),
            content_type="application/json")
            
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["message"], str)
        self.assertEqual(result['message'],"email cannot be empty")

    def test_account_creation_missing_isadmin(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
            "othername": "smith",
            "email": "johndoe@gmail.com",
            "phone": "+254724862149",
            "password":"123",
            "passporturl": "demo.com/image.jpg"
        }
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(user),
            content_type="application/json")
            
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["message"], str)
        self.assertEqual(result['message'],"isadmin cannot be empty")

    def test_account_creation_missing_phone(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
            "othername": "smith",
            "email": "johndoe@gmail.com",
            "isadmin": "False",
            "password":"123",
            "passporturl": "demo.com/image.jpg"
        }
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(user),
            content_type="application/json")
            
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["message"], str)
        self.assertEqual(result['message'],"phone cannot be empty")

    def test_account_creation_missing_password(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
            "othername": "smith",
            "email": "johndoe@gmail.com",
            "isadmin": "False",
            "phone": "+254724862149",
            "passporturl": "demo.com/image.jpg"
        }
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(user),
            content_type="application/json")
            
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["message"], str)
        self.assertEqual(result['message'],"password cannot be empty")
    
    def test_account_creation_missing_passporturl(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
            "othername": "smith",
            "email": "johndoe@gmail.com",
            "isadmin": "False",
            "phone": "+254724862149",
            "password":"123"
        }
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(user),
            content_type="application/json")
            
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["message"], str)
        self.assertEqual(result['message'], "passporturl cannot be empty")
