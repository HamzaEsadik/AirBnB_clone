#!/usr/bin/python3
"""Module for testing the Amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test Amenity class implementation"""

    def test_module_documentation(self):
        """Test documentation for the module"""
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

    def test_constructor_documentation(self):
        """Test documentation for the constructor"""
        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Validate the types of the attributes and class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)

if __name__ == '__main__':
    unittest.main()