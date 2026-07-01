#!/usr/bin/python3

import unittest
import json
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

    def test_to_json_string_normal(self):
        data = [{"id": 1, "name": "test"}]
        json_str = Base.to_json_string(data)

        self.assertEqual(type(json_str), str)
        self.assertEqual(json_str, json.dumps(data))

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")


if __name__ == '__main__':
    unittest.main()
