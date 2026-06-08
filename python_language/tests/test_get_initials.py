#!/usr/bin/python3

import unittest
from get_initials import get_initials


class TestGetInitials(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(get_initials("john", "doe"), "JD")

    def test_mixed_capitalization(self):
        self.assertEqual(get_initials("Mary", "Smith"), "MS")

    def test_single_letter_names(self):
        self.assertEqual(get_initials("a", "b"), "AB")

if __name__ == '__main__':
    unittest.main(verbosity=2)
