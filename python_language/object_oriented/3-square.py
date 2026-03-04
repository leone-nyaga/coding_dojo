#!/usr/bin/python3


class Square:
    """Represents a Square Class"""

    def __init__(self, size: int = 0) -> None:
        """
        Initializes the Square.

        Args:
            size (int): The length of one side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer!")
        if size < 0:
            raise ValueError("Size must be greater than zero!")

        self.__size = size

    def area(self) -> int:
        """
        Method that calculates Area of the Square.
        """
        return self.__size ** 2


def main() -> None:
    """
    Tests the implementation of the Square class.
    """
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))


if __name__ == '__main__':
    main()
