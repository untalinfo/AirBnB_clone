#!/usr/bin/python3
"""
Test for BaseModel
"""
import pep8
import unittest
import models
from models import base_model
from models.base_model import BaseModel

class TestDocsB(unittest.TestCase):
    """
    check for documentation
    """
    def test_module_doc(self):
        """
        check for module documentation
        """
        self.assertTrue(len(base_model.__doc__) > 0)

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

class TestBaseModel(unittest.TestCase):
    """
    Test BaseModel
    """

    def test_pep8_state(self):
        """
        test pep8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Code style errors founded.")

    def set_up(self):
        self.my_model = BaseModel()
        

if __name__ == '__main__':
    unittest.main()
