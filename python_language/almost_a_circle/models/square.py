#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new square instance.

        Args:
            size: The size of the square. (width and height).
            x: horizontal position.
            y: vertical position.
            id: Identifier that is passed from the base.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Size getter.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        String format representation.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

