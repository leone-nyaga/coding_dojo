#!/usr/bin/python3

class Square:
    """Represents a square."""

    def __init__(self, size: int = 0) -> None:
        """Initializes a new square.

        Args:
            size: length of one side of a square, default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be greater than zero")

        self.__size = size


def main() -> None:
    """Test attributes of the Square class"""
    my_square_1: Square = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2: Square = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    try:
        my_square_3: Square = Square("3")
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4: Square = Square(-89)
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
