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

    def update(self, *args, **kwargs):
        """
        Update the Square attributes using *args in order or **kwargs by key.
        """
        if args and args != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Return the dictionary representation of a Square.
        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

