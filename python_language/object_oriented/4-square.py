#!/usr/bin/python3


class Square:
    """Represents a Square class"""

    def __init__(self, size: int = 0) -> None:
        """
        Initializes the Square.

        Args:
            size: Length of one side of the Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.size = size

    @property
    def size(self) -> int:
        """
        Get the size of the square.

        Returns:
            Int: Length of the side of a square.
        """
        return self.__size

    @size.setter
    def size(self, value) -> None:
        """
        Set the size of the Square.

        Args:
            Value: The new length of a side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be greater than zero")
        self.__size = value

    def area(self) -> int:
        """
        Method that calculates area of a square
        """
        return self.__size ** 2


def main() -> None:
    """Run example usage of the Square class."""
    my_square: Square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
