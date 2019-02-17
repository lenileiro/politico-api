import json
import unittest
import instance
from app import create_app

app = create_app("testing")


class TestErrorCodes(unittest.TestCase):
    """ Test error codes 404, 405 and 500 """
    def setUp(self):
        """ Test variables """

        app.config.from_object(instance.config.Testing)
        self.client = app.test_client()

    def test_404(self):
        response = self.client.get('/api/v1')
        result = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(result['status'], 404)
    
    def test_405(self):
        """ Test error 405 """
        response = self.client.patch('/api/v1/offices')
        result = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 405)
        self.assertEqual(result['status'], 405)
