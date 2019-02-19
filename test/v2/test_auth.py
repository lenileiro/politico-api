import json
from .base import BaseTest

class TestPostRequest(BaseTest):

    def test_account_creation(self):
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
        self.assertEqual(result['data'],"user created")
    
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

    def test_account_creation_lack_national_id(self):
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

    def test_account_creation_lack_firstname(self):
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

    def test_account_creation_lack_lastname(self):
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

    def test_account_creation_lack_othername(self):
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

    def test_account_creation_lack_email(self):
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

    def test_account_creation_lack_isadmin(self):
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

    def test_account_creation_lack_phone(self):
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

    def test_account_creation_lack_password(self):
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
    
    def test_account_creation_lack_passporturl(self):
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
