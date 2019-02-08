import json
import unittest
import instance
import app

app = app.create_app("testing")

class BaseTest(unittest.TestCase):
    """ Test class for user endpoints """

    def setUp(self):
        """ Defining test variables """
        app.config.from_object(instance.config.Testing)
        self.client = app.test_client()
        self.patch_party = {
            "name": "new political party name"
        }

    def valid_delete_request(self):
        response = self.client.delete(
            "/api/v1/parties/2", content_type="application/json"
        )
        return response

    def invalid_delete_request(self):
        response = self.client.delete(
            "/api/v1/parties/10000", content_type="application/json"
        )
        return response
    
    def valid_patch_request(self):
        response = self.client.delete(
            "/api/v1/parties/1/name",data=json.dumps(self.patch_party), content_type="application/json"
        )
        return response

    def invalid_patch_request(self):
        response = self.client.delete(
            "/api/v1/parties/10000/name",data=json.dumps(self.patch_party), content_type="application/json"
        )
        return response
if __name__ == "__main__":
    unittest.main()
