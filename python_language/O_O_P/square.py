#!/usr/bin/python3


"""Define a square class"""


class square:
    """Represents a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if (size < 0):
            raise ValueError("Size must be greater than zero")

        self.__size = size

    def area(self):
        return self.__size ** 2
