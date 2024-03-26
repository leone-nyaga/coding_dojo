#!/usr/bin/python3

def outer_function(a, b):
    """
    Performs a series of operations of two numbers.

    Numbers 'a' and 'b' perform the following:
    1. Addition of 'a' and 'b'.
    2. Adds 5 from step 1.
    3. Returns final result

    Parameters:
    a: int or float
    b: int or float

    Returns:
    int or float
    """
    def inner_function():
        """
        Calculates addition of two numbers

        Returns:
        result
        """
        return a + b

    def add_five(result):
        """
        Adds 5 to a number.

        Parameters:
        result(int or float)

        Returns:
        int or float
        """
        return result + 5

        result = outer_function(3, 4)
        print(result)
