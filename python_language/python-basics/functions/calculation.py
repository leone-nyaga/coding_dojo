#!/usr/bin/python3

def calculation(a, b):
    """
    Performs addition and subtraction of two numbers.

    This functions takes two numbers and:
    1. Performs addition
    2. Performs subtraction
    3. Returns a tuple

    Parameters:
    a(int): first number.
    b(int): second number.

    Returns:
    tuple
    """
    add = a + b
    sub = a - b

    return (add, sub)

result = calculation(70, 10)
print(result)
