#!/usr/bin/python3
""" 
Unit tests for the State model.
"""


from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Test case for the State class."""

    def __init__(self, *args, **kwargs):
        """ Initializes the test case."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test the name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
