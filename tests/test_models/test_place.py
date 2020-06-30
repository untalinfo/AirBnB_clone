#!/usr/bin/python3
"""
Test for Place
"""
import pep8
import unittest
import models
from models import place
from models.base_model import BaseModel
Place = place.Place


class TestDocsB(unittest.TestCase):
    """
    check for documentation
    """
    def test_module_doc(self):
        """
        check for module documentation
        """
        self.assertTrue(len(place.__doc__) > 0)

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


class TestPlace(unittest.TestCase):
    """
    Test Place
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
        Test is Place is a BaseModel subclass
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_city_id(self):
        """
        test if city_id is an empty string
        """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id(self):
        """
        test if user_id is an empty string
        """
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_name(self):
        """
        test if name is an empty string
        """
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_description(self):
        """
        test if description an empty string
        """
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_nrooms(self):
        """
        test if number_rooms is an int
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)

    def test_nbathrooms(self):
        """
        test the number of bathrooms
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)

    def test_maxguest(self):
        """
        test max guest
        """
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(place.max_guest, 0)

    def test_price(self):
        """
        test price by night
        """
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(place.price_by_night, 0)

    def test_latitude(self):
        """test latitude"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(place.latitude, 0.0)

    def test_longitude(self):
        """
        test longitude
        """
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)

    def test_amenityids(self):
        """
        test amenity_ids
        """
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_create_to_dict(self):
        """
        test to verified if the dic is created
        """
        place = Place()
        dict_new = place.to_dict()
        self.assertEqual(type(dict_new), dict)

    def test_values_to_dict(self):
        """
        test to verified de values in a dic
        """
        place = Place()
        dict_new = place.to_dict()
        self.assertEqual(dict_new["__class__"], "Place")
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertEqual(type(dict_new["id"]), str)

    def test_is_an_instance(self):
        """check if my_model is an instance of BaseModel"""
        my_place = Place()
        self.assertIsInstance(my_place, Place)
