#!/usr/bin/python3


class Rectangle:
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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

    def __repr__(self):
        """
        string representation of the rectangle to be able
        to recreate a new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


def main():
    """Main function to test the rectangle class"""
    my_rectangle_1 = Rectangle(2, 4)
    my_rectangle_2 = Rectangle(2, 4)
    print("{:d} instances of Rectangle".format(
        Rectangle.number_of_instances))
    del my_rectangle_1
    print("{:d} instances of Rectangle".format(
        Rectangle.number_of_instances))
    del my_rectangle_2
    print("{:d} instances of Rectangle".format(
        Rectangle.number_of_instances))


if __name__ == '__main__':
    main()
