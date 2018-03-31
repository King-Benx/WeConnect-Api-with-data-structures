import unittest
from werkzeug.security import check_password_hash
from app.models import User
from app import users


class UserTestCase(unittest.TestCase):
    def setUpInstances(self):
        user = User('test', 'test@mail.com', 'password1')
        return user

    def setUpInstances2(self):
        user2 = User('test2', 'test2@mail.com', 'password2')
        return user2

    def test_class_instance(self):
        # Tests whether an object is an instance of the class
        self.assertIsInstance(self.setUpInstances(), User)

    def test_generate_password(self):
        # Tests that a password hash is unique and that its not the same as the previous value
        result = self.setUpInstances().generate_password('password1')
        result2 = self.setUpInstances2().generate_password('password2')
        self.assertNotEqual(result, result2)
        self.assertNotEqual(self.setUpInstances().password_hash, 'password')

    def test_verify_password(self):
        # Tests that we can verify a password
        result = self.setUpInstances().verify_password('password')
        self.assertTrue(
            check_password_hash(self.setUpInstances().password_hash,
                                'password1'))
        self.assertFalse(
            check_password_hash(self.setUpInstances().password_hash, 'pass'))

    def test_generate_user_id(self):
        # Tests that an id is totally random
        self.assertNotEqual(self.setUpInstances().id,
                            self.setUpInstances2().id)

    def test_username(self):
        # Tests that a username has to be unique
        self.assertNotEqual(self.setUpInstances().username,
                            self.setUpInstances2().username)

    def test_user_created(self):
        # Tests that a user has been created
        self.assertNotEqual(len(users), 0)

    def test_logout(self):
        # Tests that a user is actually logged out
        self.assertTrue(User.logout())

    def test_create_user_parameters(self):
        # Tests that a user cannot have empty parameters
        self.assertNotEqual(self.setUpInstances().username, '')
        self.assertNotEqual(self.setUpInstances().email, '')
        self.assertNotEqual(self.setUpInstances().password_hash, '')
        self.assertRaises(ValueError)

    def test_reset_password(self):
        # Tests that the username has been set
        self.setUpInstances()
        self.assertTrue(
            User.reset_password(self.setUpInstances().username, 'test'))
