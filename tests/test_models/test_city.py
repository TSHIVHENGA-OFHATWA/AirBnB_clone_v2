#!/usr/bin/python3
"""
This module contains the test class for the City model.
"""

from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ 
    Test class for the City model, inheriting from test_basemodel.
    """

    def __init__(self, *args, **kwargs):
        """ 
        Initialize the test class, setting the name and value attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test that the state_id attribute of a City instance is a string.
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Test that the name attribute of a City instance is a string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
