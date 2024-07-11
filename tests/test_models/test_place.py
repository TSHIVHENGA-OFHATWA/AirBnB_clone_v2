#!/usr/bin/python3
""" 
Unit tests for the Place model.
"""


from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
     """
    Tests for the Place class.

    Inherits from test_basemodel to utilize its setup and methods for testing.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test_Place instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Test that the city_id attribute is a string.
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Test that the user_id attribute is a string.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
       """
        Test that the name attribute is a string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        Test that the description attribute is a string.
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        Test that the number_rooms attribute is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Test that the number_bathrooms attribute is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ 
        Test that the max_guest attribute is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Test that the longitude attribute is a float.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ 
        Test that the amenity_ids attribute is a list.
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
