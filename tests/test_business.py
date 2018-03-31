import unittest
from app.models import Business
from app import businesses, known_business_ids
from flask import session


class BusinessTestCase(unittest.TestCase):
    def setUpBusinessInstance(self):
        business = Business(1, 'test business', 'inland', 'technology',
                            'business description')
        return business

    def setUpBusinessInstance2(self):
        business2 = Business(1, 'test business', 'overseas', 'technology',
                             'business description')
        return business2

    def test_class_instance(self):
        # Tests that an object is an instance of a class
        self.assertIsInstance(self.setUpBusinessInstance(), Business)

    def test_generate_business_id(self):
        # Tests that a unique id is created
        self.assertNotEqual(self.setUpBusinessInstance().id,
                            self.setUpBusinessInstance2().id)

    def test_create_business(self):
        # Tests to check whether a business has been created
        self.setUpBusinessInstance()
        self.assertNotEqual(len(businesses), 0)
        self.assertRaises(ValueError)

    def test_update_business(self):
        # Tests whether a business has been updated
        self.assertTrue(self.setUpBusinessInstance().update_business(
            1,
            self.setUpBusinessInstance().id, 'update business', 'inland',
            'technology', 'business description'))

    def test_delete_business(self):
        # Tests whether an owner of a business has deleted a business
        self.setUpBusinessInstance()
        self.setUpBusinessInstance2()
        business_status = Business.delete_business(
            self.setUpBusinessInstance2().user_id,
            self.setUpBusinessInstance2().id)
        self.assertTrue(business_status)

    def test_get_all_businesses(self):
        # Tests that a list of information is returned
        self.assertIs(type(Business.get_all_businesses()), list)

    def test_retrieve_a_business(self):
        # Tests that a business id exists
        self.setUpBusinessInstance()
        self.assertIn(self.setUpBusinessInstance().id, known_business_ids)
        self.assertIs(
            type(Business.get_business_by_id(self.setUpBusinessInstance().id)),
            list)
