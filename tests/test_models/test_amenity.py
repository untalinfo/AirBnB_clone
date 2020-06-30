#!/usr/bin/python3
"""
Test for Amenity
"""
import pep8
import unittest
import models
from models import amenity
from models.base_model import BaseModel
Amenity = amenity.Amenity


class TestDocsB(unittest.TestCase):
    """
    check for documentation
    """
    def test_module_doc(self):
        """
        check for module documentation
        """
        self.assertTrue(len(amenity.__doc__) > 0)

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


class TestAmenity(unittest.TestCase):
    """
    Test Amenity
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
        Test if Amenity is a BaseModel subclass
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name(self):
        """
        test if name is an empty string
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_create_to_dict(self):
        """
        test to verified if the dic is created
        """
        amenity = Amenity()
        dict_new = amenity.to_dict()
        self.assertEqual(type(dict_new), dict)

    def test_values_to_dict(self):
        """
        test to verified de values in a dic
        """
        amenity = Amenity()
        dict_new = amenity.to_dict()
        self.assertEqual(dict_new["__class__"], "Amenity")
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertEqual(type(dict_new["id"]), str)

    def test_is_an_instance(self):
        """
        check if my_amenity is an instance of Amenity
        """
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)
