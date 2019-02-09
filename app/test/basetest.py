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
        self.edit_party = {
            "name": "new political party name"
        }

        self.create_party_1 ={
            "name" : 'party C',
            "hqAddress" : 'box 148, Nairobi',
            "logoUrl" : 'https://via.placeholder.com/150' 
        }

        self.create_party_2 ={
            "name" : 'party C',
            "logoUrl" : 'https://via.placeholder.com/150' 
        }

        self.create_party_3 ={
            "name" : 'party C',
            "hqAddress" : 'box 148, Nairobi'
        }
        self.create_party_4 ={
            "hqAddress" : 'box 148, Nairobi',
            "logoUrl" : 'https://via.placeholder.com/150' 
        }
        self.create_office_1 = {
                "type" : 'national',
                "name": "President"
            }
        self.create_office_2 = {
                "type" : 'national'
            }
        self.create_office_3 = {
                "name": "President"
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

    def valid_get_request(self):
        response = self.client.get(
            "/api/v1/parties/", content_type="application/json"
        )
        return response
    
    def valid_individual_get_request(self):
        response = self.client.get(
            "/api/v1/parties/1", content_type="application/json"
        )
        return response
    
    def valid_individual_office_get_request(self):
        response = self.client.get(
            "/api/v1/offices/1", content_type="application/json"
        )
        return response
    
    def valid_office_get_request(self):
        response = self.client.get(
            "/api/v1/offices", content_type="application/json"
        )
        return response
        
    def valid_patch_request(self):
        response = self.client.patch('/api/v1/parties/1/name', data=json.dumps(self.edit_party),
                                        content_type="application/json")
            
        return response

    def invalid_patch_request(self):
        response = self.client.patch('/api/v1/parties/10000/name', data=json.dumps(self.edit_party),
                                        content_type="application/json")
        return response
    
    def valid_post_request(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.create_party_1),
                                        content_type="application/json")
            
        return response
    
    def invalid_post_request_1(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.create_party_2),
                                        content_type="application/json")
            
        return response
    
    def invalid_post_request_2(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.create_party_3),
                                        content_type="application/json")
            
        return response
    
    def invalid_post_request_3(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.create_party_4),
                                        content_type="application/json")
            
        return response
    
    def valid_office_post_request(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.create_office_1),
                                        content_type="application/json")
            
        return response
    
    def invalid_office_post_request_1(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.create_office_2),
                                        content_type="application/json")
            
        return response
    
    def invalid_office_post_request_2(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.create_office_3),
                                        content_type="application/json")
            
        return response

if __name__ == "__main__":
    unittest.main()
