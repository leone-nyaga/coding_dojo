#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Tests the Base class.
    """
    def test_id(self):
        """
        Tests the assignment of ids.
        """
        obj = Base()
        obj1 = Base(67)

        self.assertEqual(obj.id, 1, "First object should have ID 1")
        self.assertEqual(obj1.id, 67, "First object should have ID 67")


if __name__ == '__main__':
    unittest.main()
