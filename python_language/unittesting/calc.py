#!/usr/bin/python3

"""Calculations class that calculates some math operations"""


class Calculations:
    self.__a = a
    self.__b = b

    """Function that handles the sum"""
    def add(self):
        return self.__a + self.__b

    """Functions that handles the subtraction"""
    def subtract(self):
        return self.__a - self.__b

    """Function that handles the multiplications"""
    def multiply(self):
        return self.__a * self.__b

    """Function that handles division"""
    def divide(self):
        if self.__b == 0:
            raise ZeroDivisionError("Division by Zero is undefined")
        return self.__a / self.__b
