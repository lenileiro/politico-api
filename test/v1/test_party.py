import json
from .base import BaseTest


class TestDeleteRequest(BaseTest):
    def test_invalid_delete_request(self):
        response = self.client.delete(
            "/api/v1/parties/10000", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["data"][0]["message"], "Party Id not found")

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

    def test_invalid_individual_get_request(self):
        response = self.client.get(
            "/api/v1/parties/1000000221", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["status"], 404)


class TestPatchRequest(BaseTest):
    def test_invalid_patch_request(self):
        edit_party = {
            "name": "new political party name"
        }
        response = self.client.patch(
            '/api/v1/parties/10000/name', 
            data=json.dumps(edit_party), content_type="application/json")

        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["status"], 404)
        self.assertEqual(result["data"]["message"], "party not found")

    def test_valid_patch_request(self):
        edit_party = {
            "name": "new political party name"
        }
        response = self.client.patch(
            '/api/v1/parties/1/name', data=json.dumps(edit_party),
            content_type="application/json")

        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["data"][0]["name"], "new political party name")

    def test_invalid_name_patch_request(self):
        response = self.client.patch(
            '/api/v1/parties/1/name', data=json.dumps({}),
            content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)


class TestPostRequest(BaseTest):
    def test_valid_post_request(self):
        create_party = {
            "name": 'party C',
            "hqAddress": 'box 148, Nairobi',
            "logoUrl": 'https://via.placeholder.com/150' 
        }
        response = self.client.post(
            '/api/v1/parties', data=json.dumps(create_party),
            content_type="application/json")

        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"][0]["name"], "party C")

    def test_invalid_post_request_1(self):
        create_party = {
            "name": 'party C',
            "logoUrl": 'https://via.placeholder.com/150' 
        }
        response = self.client.post(
            '/api/v1/parties', data=json.dumps(create_party),
            content_type="application/json")

        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], "address cannot be empty")

    def test_invalid_post_request_2(self):
        create_party = {
            "name": 'party C',
            "hqAddress": 'box 148, Nairobi'
        }
        response = self.client.post(
            '/api/v1/parties', data=json.dumps(create_party),
            content_type="application/json")

        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], "Logo cannot be empty")

    def test_invalid_post_request_3(self):
        create_party = {
            "hqAddress": 'box 148, Nairobi',
            "logoUrl": 'https://via.placeholder.com/150' 
        }
        response = self.client.post(
            '/api/v1/parties', data=json.dumps(create_party),
            content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], "Name cannot be empty")
