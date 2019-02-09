import json
from .base_test import BaseTest

from utils.dummy import create_party_1,create_party_2,create_party_3,create_party_4,edit_party

class TestDeleteRequest(BaseTest):    
    def test_invalid_delete_request(self):
        response = self.client.delete(
            "/api/v1/parties/10000", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "Id not found")
    
    def test_valid_delete_request(self):
        response = self.client.delete(
            "/api/v1/parties/2", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["data"][0]["message"], "delete successful")

class TestGetRequest(BaseTest):    
    def test_valid_get_request(self):
        response = self.client.get(
            "/api/v1/parties/", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)

    def test_valid_individual_get_request(self):
        response = self.client.get(
            "/api/v1/parties/1", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["data"][0]["id"], 1)

class TestPatchRequest(BaseTest):    
    def test_invalid_patch_request(self):
        response = self.client.patch('/api/v1/parties/10000/name', data=json.dumps(edit_party), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "Id not found")

    def test_valid_patch_request(self):
        response = self.client.patch('/api/v1/parties/1/name', data=json.dumps(edit_party), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["data"][0]["name"], "new political party name")

class TestPostRequest(BaseTest):    
    def test_valid_post_request(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(create_party_1), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"][0]["name"], "party C")

    def test_invalid_post_request_1(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(create_party_2), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "some required fields missing")
    
    def test_invalid_post_request_2(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(create_party_3), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "some required fields missing")
    
    def test_invalid_post_request_3(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(create_party_4), content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "some required fields missing")