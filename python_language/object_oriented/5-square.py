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

    def my_print(self):
        """
        prints in stdout the square with the character '#'.
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)


def main() -> None:
    """Run example usage of the Square class."""
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")


if __name__ == '__main__':
    main()
