#!/usr/bin/python3
from mensuration import Mensuration

class Circle(Mensuration):
    """
    Represents a circle. A circle is a shape where the radius is the same
    in all directions (width = height = radius).

    Attributes:
        side_x (float): The radius of the circle (used for both width and height).
        side_y (float): The radius of the circle (same as side_x for a circle).
    """
    def __init__(self, radius: float) -> None:
        """
        Initializes the Circle object with the given radius.

        Args:
            radius (float): The radius of the circle.
        """
        super().__init__(radius, radius)  # In a circle, side_x and side_y are both the radius

    def area(self) -> float:
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle, calculated as π * radius^2.
        """
        return 3.14159 * self.side_x ** 2  # π * radius^2

    def perimeter(self) -> float:
        """
        Calculates the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle, calculated as 2 * π * radius.
        """
        return 2 * 3.14159 * self.side_x  # 2 * π * radius

    def __str__(self) -> str:
        """
        Returns a string representation of the Circle.

        Returns:
            str: A string describing the circle's radius.
        """
        return f"Circle: radius = {self.side_x}"

