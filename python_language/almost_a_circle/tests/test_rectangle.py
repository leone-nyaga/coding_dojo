#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Unittest class for Rectangle Class.
    """
    def test_initialization(self):
        """
        Test if initialization is implemented correctly.
        """
        rect = Rectangle(5, 10, 2, 3, 1)

        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
