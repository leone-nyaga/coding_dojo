#!/usr/bin/python3

class Square:
    def __init__(self, size=0):

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("must be greater than zero")
            
            self.__size = value

        def area(self):
            return self.__size ** 2

        def my_print(self):
            """Print the square with the # character."""
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
                if self.__size == 0:
                    print("")
