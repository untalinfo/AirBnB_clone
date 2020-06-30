#!/usr/bin/python3
"""
Test for City
"""
import pep8
import unittest
import models
from models import city
from models.base_model import BaseModel
City = city.City


class TestDocsB(unittest.TestCase):
    """
    check for documentation
    """
    def test_module_doc(self):
        """
        check for module documentation
        """
        self.assertTrue(len(city.__doc__) > 0)

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


class TestCity(unittest.TestCase):
    """
    Test City
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
        Test if City is a BaseModel subclass
        """
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name(self):
        """
        test if name is an empty string
        """
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_state_id(self):
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_create_to_dict(self):
        """
        test to verified if the dic is created
        """
        city = City()
        dict_new = city.to_dict()
        self.assertEqual(type(dict_new), dict)

    def test_values_to_dict(self):
        """te
        st to verified de values in a dic
        """
        city = City()
        dict_new = city.to_dict()
        self.assertEqual(dict_new["__class__"], "City")
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertEqual(type(dict_new["id"]), str)

    def test_is_an_instance(self):
        """
        check if my_model is an instance of BaseModel
        """
        my_city = City()
        self.assertIsInstance(my_city, City)
