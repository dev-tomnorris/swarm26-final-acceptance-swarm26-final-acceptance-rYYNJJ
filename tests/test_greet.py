import unittest

from src.greet import greet

class GreetTests(unittest.TestCase):
    def test_greet_uses_welcome(self):
        self.assertEqual(greet("Waggle"), "Welcome, Waggle!")
