import unittest
from calc.py import Calculations


"""Unittest Class for the class Calculations"""
class TestCalculations(unittest.TestCase):

    """Test for the function add"""
    def test_add(self):
        calc = Calculations(10, 5)
        self.assertEqual(calc(), 15)

    """Test for the function subtract"""
    def test_subtract(self):
        calc = Calculations(10, 5)
        self.assertEqual(calc(), 5)

    """Test for the Function multiply"""
    def test_multiply(self):
        calc = Calculations(10, 5)
        self.assertEqual(calc(), 2)

    """Testcase for the ZeroDivisionError exception"""
    def test_divide_by_zero(self):
        calc = Calculations(10, 0)
        with self.assertRaises(ZeroDivisionError):
            calc.divide()

if __name__ == "__main__":
    unitest.main()
