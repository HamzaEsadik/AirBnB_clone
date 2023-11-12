#!/usr/bin/python3
"""Test cases for the Review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test Review class implementation"""

    def test_module_documentation(self):
        """Test documentation for the module"""
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)

    def test_constructor_documentation(self):
        """Test documentation for the constructor"""
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Validate the types of the attributes and class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)


if __name__ == '__main__':
    unittest.main()
