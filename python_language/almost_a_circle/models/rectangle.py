#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width: Width of rectangle.
            height: Height of rectagle.
            x: Horizontal position.
            y: Vertical position.
            id: identifier passed to Base.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter to width.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Witdh must be greater than zero")
        self.__width = value

    @property
    def height(self):
        """
        Getter to height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter to height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("Height must be greater than zero")
        self.__height = value

    @property
    def x(self):
        """
        Getter to x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter to x.
        """
        if not isinstance(value, int):
            raise TypeError("X must be an integer")
        if value < 0:
            raise ValueError("X must be greater than zero")
        self.__x = value

    @property
    def y(self):
        """
        Getter to y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter to y.
        """
        if not isinstance(value, int):
            raise TypeError("X must be an integer")
        if value < 0:
            raise ValueError("X must be greater than zero")
        self.__y = value

    def area(self):
        """
        Function that calculates the area of a rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints rectangle instance with the '#' character.
        """
        for _ in range(self.__height):

