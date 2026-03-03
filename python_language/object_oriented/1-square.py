#!/usr/bin/python3


class Square:
    """A square class"""

    def __init__(self, size: int) -> None:
        """Initialize a new square.

        Args:
            size: length of one side of a square.
        """
        self.__size: int = size


def main() -> None:
    """Test attribute access behavior."""
    my_square: Square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
