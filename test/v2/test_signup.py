import json
from .base_test import BaseTest

class TestPostRequest(BaseTest): 
    def test_create_account(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
            "othername": "smith",
            "email": "johndoe@gmail.com",
            "isadmin": "False",
            "phone": "+254724862149",
            "password":"pbkdf2:sha256:50000$y9DI0W56$dbc0ccc48dd099ebcafdf49be84273c81b3618fdbf7a1f67cb30bf9655a2ce38",
            "passporturl": "https://demo.com/image.jpg"
        }
        response = self.client.post(
            "/api/v2/auth/signup",data=json.dumps(user), content_type="application/json")
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

    def test_create_account_missing_national_id(self):
        user = {
            "firstname": "John",
            "lastname": "Joe",
            "othername": "smith",
            "email": "johndoe@gmail.com",
            "isadmin": "False",
            "phone": "+254724862149",
            "password":"123",
            "passporturl": "https://demo.com/image.jpg"
        }
        response = self.client.post(
            "/api/v2/auth/signup",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
       
    def test_create_account_missing_firstname(self):
        user = {
	        "national_id": 32308961,
            "lastname": "Joe",
            "othername": "smith",
            "email": "johndoe@gmail.com",
            "isadmin": "False",
            "phone": "+254724862149",
            "password":"123",
            "passporturl": "https://demo.com/image.jpg"
        }
        response = self.client.post(
            "/api/v2/auth/signup",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)

    def test_create_account_missing_lastname(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "othername": "smith",
            "email": "johndoe@gmail.com",
            "isadmin": "False",
            "phone": "+254724862149",
            "password":"123",
            "passporturl": "https://demo.com/image.jpg"
        }
        response = self.client.post(
            "/api/v2/auth/signup",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)

    def test_create_account_missing_othername(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
            "email": "johndoe@gmail.com",
            "isadmin": "False",
            "phone": "+254724862149",
            "password":"123",
            "passporturl": "https://demo.com/image.jpg"
        }
        response = self.client.post(
            "/api/v2/auth/signup",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
    
    def test_create_account_missing_email(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
            "othername": "smith",
            "isadmin": "False",
            "phone": "+254724862149",
            "password":"123",
            "passporturl": "https://demo.com/image.jpg"
        }
        response = self.client.post(
            "/api/v2/auth/signup",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
    
    def test_create_account_missing_isadmin(self):
        user = {
           "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
            "othername": "smith",
            "email": "johndoe@gmail.com",
            "phone": "+254724862149",
            "password":"123",
            "passporturl": "https://demo.com/image.jpg"
        }
        response = self.client.post(
            "/api/v2/auth/signup",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
    
    def test_create_account_missing_phone(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
            "othername": "smith",
            "email": "johndoe@gmail.com",
            "isadmin": "False",
            "password":"123",
            "passporturl": "https://demo.com/image.jpg"
        }
        response = self.client.post(
            "/api/v2/auth/signup",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
    
    def test_create_account_missing_password(self):
        user = {
            "national_id": 32308961,
            "firstname": "John",
            "lastname": "Joe",
            "othername": "smith",
            "email": "johndoe@gmail.com",
            "isadmin": "False",
            "phone": "+254724862149",
            "passporturl": "https://demo.com/image.jpg"
        }
        response = self.client.post(
            "/api/v2/auth/signup",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
    
    def test_create_account_missing_passporturl(self):
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
            "/api/v2/auth/signup",data=json.dumps(user), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)