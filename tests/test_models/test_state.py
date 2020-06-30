#!/usr/bin/python3
"""
Test for State
"""
import pep8
import unittest
import models
from models import state
from models.base_model import BaseModel
State = state.State

class TestDocsB(unittest.TestCase):
    """
    check for documentation
    """
    def test_module_doc(self):
        """
        check for module documentation
        """
        self.assertTrue(len(state.__doc__) > 0)

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

class TestState(unittest.TestCase):
    """
    Test State
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
        Test if State is a BaseModel subclass
        """
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_name(self):
        """
        test if name is an empty string
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_create_to_dict(self):
        """
        test to verified if the dic is created
        """
        state = State()
        dict_new = state.to_dict()
        self.assertEqual(type(dict_new), dict)

    def test_values_to_dict(self):
        """
        test to verified de values in a dic
        """
        state = State()
        dict_new = state.to_dict()
        self.assertEqual(dict_new["__class__"], "State")
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertEqual(type(dict_new["id"]), str)

    def test_is_an_instance(self):
        """
        check if my_state is an instance of State
        """
        my_state = State()
        self.assertIsInstance(my_state, State)
