#!/usr/bin/python3
from mensuration import Mensuration


class Square(Mensuration):
    """
    Represents a square. A square is a special case of a rectangle
    where both sides are of equal length.

    Attributes:
        side_x (float): The length of one side of the square.
        side_y (float): The length of one side of the square (same as side_x for a square).
    """
    def __init__(self, side: float) -> None:
        """
        Initializes the Square object with the given side length.

        Args:
            side (float): The length of the side of the square.
        """
        super().__init__(side, side)  # Both side_x and side_y are the same for a square

    def area(self) -> float:
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square, calculated as side^2.
        """
        return self.side_x ** 2

    def perimeter(self) -> float:
        """
        Calculates the perimeter of the square.

        Returns:
            float: The perimeter of the square, calculated as 4 * side.
        """
        return 4 * self.side_x

    def __str__(self) -> str:
        """
        Returns a string representation of the Square.

        Returns:
            str: A string describing the square's side length.
        """
        return f"Square: side = {self.side_x}"

