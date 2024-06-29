#!/usr/bin/python3
""" 
Unit tests for the Review class.
"""


from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """
    Test case for the Review class.

    Inherits test cases from test_basemodel and specifically tests Review attributes.

    Attributes:
        name (str): The name of the test class ('Review').
        value (class): The Review class being tested.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the test case.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        Test case for the place_id attribute of the Review class.

        Creates a new instance of Review and asserts that place_id is of type str.
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Test case for the user_id attribute of the Review class.

        Creates a new instance of Review and asserts that user_id is of type str.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Test case for the text attribute of the Review class.

        Creates a new instance of Review and asserts that text is of type str.
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
