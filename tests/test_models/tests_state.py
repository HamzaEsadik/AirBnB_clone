#!/usr/bin/python3
"""Test cases for the State class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test State class implementation"""

    def test_module_documentation(self):
        """Test documentation for the module"""
        doc = State.__doc__
        self.assertGreater(len(doc), 1)

    def test_constructor_documentation(self):
        """Test documentation for the constructor"""
        doc = State.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Validate the types of the attributes and class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)


if __name__ == '__main__':
    unittest.main()
