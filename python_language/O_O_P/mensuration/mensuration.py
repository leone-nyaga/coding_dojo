#!/usr/bin/python3

class Mensuration:
    """
    This is the base class that performs geometric measurements.

    Subclasses must implement area() and perimeter() methods.
    """


    def __init__(self, side_x: float, side_y: float = None) -> None:
        """
        Initializes the Munsuration class.

        Args:
            side_x (float): Length of first side
            side_y (float, optional): Length of second side.
                                      Defaults to none if shape requires only one side
        """
        self.side_x = side_x
        self.side_y = side_y

    def area(self) -> float:
        """
        Calculates Area of the shape.

        Returns:
            Float: The area of the shape.
        """
        return NotImplementedError("Subclass should implement this method")

    def perimeter(self) -> float:
        """
        Calculates Perimeter of the shape.

        Returns:
            Float: Perimeter of the shape.
        """
        return NotImplementedError("Subclass should implement this method")

    def __str__(self):
        """
        Represents the string representation of the Mensuration object.

        Returns:
            str: String describing sides of the shape
        """
        return f"Mensuration: side_x = {self.side_x}, side_y = {self.side_y if self.side_y is not None else 'N/A'}"
            
