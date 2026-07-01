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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be greater than zero")
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
            raise ValueError("height must be greater than zero")
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
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be greater than zero")
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
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be greater than zero")
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
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end=" ")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Prints the Rectangle representation in a particular format.
        """
        return (
                f"[Rectangle] ({self.id}) " 
                f"{self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}"
                )

    def update(self, *args, **kwargs):
        """
        Update the Rectangle attributes using *args in
        order or **kwargs by key.
        """
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]

            if len(args) >= 2:
                self.width = args[1]

            if len(args) >= 3:
                self.height = args[2]

            if len(args) >= 4:
                self.x = args[3]

            if len(args) >= 5:
                self.y = args[4]

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]

            if "width" in kwargs:
                self.width = kwargs["width"]

            if "height" in kwargs:
                self.height = kwargs["height"]

            if "x" in kwargs:
                self.x = kwargs["x"]

            if "y" in kwargs:
                self.y = kwargs["y"]
