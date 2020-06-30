#!/usr/bin/python3
"""
Test for User
"""
import pep8
import unittest
import models
from models import user
from models.base_model import BaseModel
User = user.User

class TestDocsB(unittest.TestCase):
    """
    check for documentation
    """
    def test_module_doc(self):
        """
        check for module documentation
        """
        self.assertTrue(len(user.__doc__) > 0)

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

class TestUser(unittest.TestCase):
    """
    Test User
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
        Test is User is a BaseModel subclass
        """
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_email(self):
        """
        test if email is an empty string
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password(self):
        """
        test if password is an empty string
        """
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_fist_name(self):
        """
        test if first_name is an empty string
        """
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name(self):
        """
        test if last_name s an empty string
        """
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_create_to_dict(self):
        """
        test to verified if the dic is created
        """
        user = User()
        dict_new = user.to_dict()
        self.assertEqual(type(dict_new), dict)

    def test_values_to_dict(self):
        """
        test to verified de values in a dic
        """
        user = User()
        dict_new = user.to_dict()
        self.assertEqual(dict_new["__class__"], "User")
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertEqual(type(dict_new["id"]), str)

    def test_is_an_instance(self):
        """
        check if my_model is an instance of BaseModel
        """
        my_user = User()
        self.assertIsInstance(my_user, User)
