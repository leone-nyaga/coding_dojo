#!/usr/bin/python3


def add(a, b):
    """
    Function that returns the sum of two numbers.

    Args:
        a: integer
        b: integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        return TypeError("Both arguments must be integers")

    return a + b


def main():
    """
    Function that tests the add function.
    """
    a = 20
    b = 15

    result = add(a, b)

    print(result)


if __name__ == '__main__':
    main()
