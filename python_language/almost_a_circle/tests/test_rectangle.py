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

    def test_area(self):
        """
        Tests if the area function is defined correctly.
        """
        rect1 = Rectangle(5, 10)

        self.assertEqual(rect1.area(), 50)

    def test_str(self):
        """
        Tests if the str method have been overwritten successfully.
        """
        rect2 = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6"

        self.assertEqual(str(rect2), expected)

    def test_to_dictionary(self):
        """
        Tests if the to_dictionary method will return a dictionary.
        """
        r = Rectangle(10, 2, 1, 9, 1)
        r_dict = r.to_dictionary()

        self.assertEqual(type(r_dict), dict)

        expected_keys = ["id", "width", "height", "x", "y"]
        self.assertEqual(sorted(r_dict.keys()), sorted(expected_keys))

        self.assertEqual(r_dict["id"], 1)
        self.assertEqual(r_dict["width"], 10)
        self.assertEqual(r_dict["height"], 2)
        self.assertEqual(r_dict["x"], 1)
        self.assertEqual(r_dict["y"], 9)



if __name__ == '__main__':
    unittest.main(verbosity=2)
