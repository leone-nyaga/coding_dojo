#!/usr/bin/python3

from typing import Union


def add_numbers(
        a: Union[int, float],
        b: Union[int, float]
        ) -> Union[int, float, str]:
    """
    Adds two numbers as long as both inputs are int or float.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b
    str: Error message if either input is not a number.
    """

    if isinstance(a, (int, float)) and isinstance(a, (int, float)):
        return a + b
    else:
        return "Both inputs must be numbers"

def main():
    print(add_numbers(2, 3))
    print(add_numbers(12.4, 7.8))
    print(add_numbers("10", 7))
    print(add_numbers("9.9", 11))

if __name__ == "__main__":
    main()
