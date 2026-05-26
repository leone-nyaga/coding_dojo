#!/usr/bin/python3


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle.
        Args:
            width: width of rectangle.
            height: height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter to the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be greater than zero")
        self.__width = value

    @property
    def height(self):
        """Getter to height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to height"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be greater than zero")
        self.__height = value

    def area(self):
        """Method that returns area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """method that returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Method that prints string representations of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        result = ""

        for h in range(self.__height):
            for w in range(self.__width):
                result += "#"

            if h != self.__height - 1:
                result += "\n"

        return result


def main():
    """Main function to test the rectangle class"""
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(
        my_rectangle.area(),
        my_rectangle.perimeter()))

    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))


if __name__ == '__main__':
    main()
