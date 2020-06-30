#!/usr/bin/python3
"""
Test for State
"""
import pep8
import unittest
import models
from models import review
from models.base_model import BaseModel
Review = review.Review

class TestDocsB(unittest.TestCase):
    """
    check for documentation
    """
    def test_module_doc(self):
        """
        check for module documentation
        """
        self.assertTrue(len(review.__doc__) > 0)

    def test_class_doc(self):
        """
        check for documentation
        """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """
        check for method documentation
        """
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)

class TestRiview(unittest.TestCase):
    """
    Test Review
    """

    def test_pep8_state(self):
        """
        test pep8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Code style errors founded.")

    def test_subclass(self):
        """
        Test if Review is a BaseModel subclass
        """
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_text(self):
        """
        test if text is an empty string
        """
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

    def test_place_id(self):
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_user_id(self):
        """
        test user_id
        """
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")

    def test_create_to_dict(self):
        """
        test to verified if the dic is created
        """
        review = Review()
        dict_new = review.to_dict()
        self.assertEqual(type(dict_new), dict)

    def test_values_to_dict(self):
        """
        test to verified de values in a dic
        """
        review = Review()
        dict_new = review.to_dict()
        self.assertEqual(dict_new["__class__"], "Review")
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertEqual(type(dict_new["id"]), str)

    def test_is_an_instance(self):
        """
        check if my_model is an instance of BaseModel
        """
        my_review = Review()
        self.assertIsInstance(my_review, Review)
