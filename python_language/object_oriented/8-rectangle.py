#!/usr/bin/python3


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

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

        line = str(self.print_symbol) * self.__width

        result = ""

        for h in range(self.__height):
                result += line

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2


def main():
    """Main function to test the rectangle class"""
    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if my_rectangle_1 is Rectangle.bigger_or_equal(
            my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

    my_rectangle_2.width = 10
    my_rectangle_2.height = 5

    if my_rectangle_1 is Rectangle.bigger_or_equal(
            my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")


if __name__ == '__main__':
    main()
