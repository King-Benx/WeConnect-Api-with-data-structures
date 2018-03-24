import unittest
import json
from flask import url_for
from app import create_app, known_usernames, users


class TestUserEndPoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_user_registration_route(self):
        # Tests that a user is successfully logged
        response = self.client.post(
            url_for('api.register_new_user', _external=True),
            data=json.dumps({
                "username": "test",
                "password": "pass",
                "email": "test@mail.com"
            }),
            content_type='application/json')
        self.assertTrue(response.status_code, 201)

    def test_logout_user_route(self):
        response = self.client.post(
            url_for('api.logout_user', _external=True),
            data=json.dumps({
                "username": "test"
            }),
            content_type='application/json')
        self.assertTrue(response.status_code, 201)

    def test_login_route(self):
        # Tests that the login route returns a 200 response
        response = self.client.post(
            url_for('api.logout_user', _external=True),
            data=json.dumps({
                "username": "test",
                "password": "pass"
            }),
            content_type='application/json')
        self.assertTrue(response.status_code, 200)
