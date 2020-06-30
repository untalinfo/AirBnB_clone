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

    def setUp(self):
        """
        initial values
        """
        self.my_model = BaseModel()
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

    def test_save(self):
        before = self.my_model.updated_at
        self.my_model.save()
        after = self.my_model.updated_at
        self.assertIsNot(before, after)

    def test_id(self):
        """
        test if the id of two instances are different
        """
        my_model = BaseModel()
        my_model1 = BaseModel()
        self.assertNotEqual(my_model.id, my_model1.id)

    def test_to_dict(self):
        """
        check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format.
        """
        my_model3 = BaseModel()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'BaseModel':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)

if __name__ == '__main__':
    unittest.main()
