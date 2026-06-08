#!/usr/bin/python3

import unittest
from is_even import is_even


class TestIsEven(unittest.TestCase):

    def test_even_nember(self):
        self.assertTrue(is_even(2))

    def test_odd_number(self):
        self.assertFalse(is_even(3))

    def test_negative_number(self):
        self.assertTrue(is_even(-2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
