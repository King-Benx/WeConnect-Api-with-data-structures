import unittest
import json
from flask import url_for
from app import create_app, known_usernames, users


class TestBusinessEndPoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_business_registration_route(self):
        # Tests that a business is successfully registered
        response = self.client.post(
            url_for('api.register_business', _external=True),
            data=json.dumps({
                "name": "business 1",
                "location": "location 1",
                "category": "category 1",
                "description": "description 1"
            }),
            content_type='application/json')
        self.assertTrue(response.status_code, 201)

    def test_update_business_route(self):
        response = self.client.put(
            url_for('api.update_business',businessId=1, _external=True),
            data=json.dumps({
                "name": "",
                "location": "soroti",
                "category": "",
                "description": ""
            }),
            content_type='application/json')
        self.assertTrue(response.status_code, 201)
    
    def test_delete_business_route(self):
        response = self.client.delete(
            url_for('api.delete_business',businessId=1, _external=True),
            content_type='application/json')
        self.assertTrue(response.status_code, 201)
        
        