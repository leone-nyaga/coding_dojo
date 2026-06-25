#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Multiple tests on the Square class.
    """
    def test_attributes(self):
        """
        Tests if the attributes have been defined properly.
        """
        s1 = Square(5, 2, 3, 99)

        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 99)

    def test_str(self):
        """
        Tests the str function.
        """
        s2 = Square(5, 2, 3, 99)

        expected = "[Square] (99) 2/3 - 5"
        self.assertEqual(str(s2), expected)


if __name__ == '__main__':
    unittest.main()
