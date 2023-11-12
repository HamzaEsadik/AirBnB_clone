#!/usr/bin/python3
"""Test cases for the City class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test City class implementation"""

    def test_module_documentation(self):
        """Test documentation for the module"""
        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_constructor_documentation(self):
        """Test documentation for the constructor"""
        doc = City.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Validate the types of the attributes and class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)


if __name__ == '__main__':
    unittest.main()
