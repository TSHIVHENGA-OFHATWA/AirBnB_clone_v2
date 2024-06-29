#!/usr/bin/python3
"""
Unit tests for User model in the application.

This module contains unit tests for the User model, which includes tests
for attributes like first_name, last_name, email, and password.
"""


from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """
    Unit tests for the User model class.

    This class inherits from test_basemodel and defines unit tests for
    the User model's attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test case for User model.

        Args:
            *args: Positional arguments to pass to the parent class.
            **kwargs: Keyword arguments to pass to the parent class.
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Test the first_name attribute of the User model.

        This test checks that the first_name attribute of a new User
        instance is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        Test the last_name attribute of the User model.

        This test checks that the last_name attribute of a new User
        instance is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        Test the email attribute of the User model.

        This test checks that the email attribute of a new User
        instance is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        Test the password attribute of the User model.

        This test checks that the password attribute of a new User
        instance is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.password), str)
