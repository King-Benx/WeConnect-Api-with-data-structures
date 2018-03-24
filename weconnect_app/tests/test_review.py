import unittest
from app.models import Review
from app import reviews


class ReviewTestCase(unittest.TestCase):
    def setUpReviewInstance(self):
        # create an instance of class
        review1 = Review(1, 1, 'review 1')
        return review1

    def setUpReviewInstance2(self):
        # create instance 2 of class
        review2 = Review(1, 1, 'review 2')
        return review2

    def test_class_is_instance(self):
        # Tests that an object is an instance
        self.assertIsInstance(self.setUpReviewInstance(), Review)

    def test_generate_review_id(self):
        # Tests that a unique id is created
        self.assertNotEqual(self.setUpReviewInstance().id,
                            self.setUpReviewInstance2().id)

    def test_create_business(self):
        # Tests to check whether a review has been created
        self.setUpReviewInstance()
        self.assertNotEqual(len(reviews), 0)
