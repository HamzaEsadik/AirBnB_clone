#!/usr/bin/python3
"""Unit Tests for the Console"""

import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test class for the HBNBCommand class"""

    def create_instance(self):
        """Create an instance of the HBNBCommand class"""
        return HBNBCommand()

    def test_quit_command(self):
        """Test the 'quit' command"""
        console_instance = self.create_instance()
        self.assertTrue(console_instance.onecmd("quit"))

    def test_eof_command(self):
        """Test the 'EOF' command"""
        console_instance = self.create_instance()
        self.assertTrue(console_instance.onecmd("EOF"))
