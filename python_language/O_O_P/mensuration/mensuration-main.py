#!/usr/bin/python3

from rect import Rectangle
from square import Square
from circle import Circle

if __name__ == "__main__":
    # Test case for Rectangle
    rect = Rectangle(4, 5)  # A rectangle with length 4 and width 5
    print(f"Rectangle: area = {rect.area()}, perimeter = {rect.perimeter()}")
    # Expected Output:
    # Rectangle: area = 20, perimeter = 18

    # Test case for Square
    square = Square(4)  # A square with side length 4
    print(f"Square: area = {square.area()}, perimeter = {square.perimeter()}")
    # Expected Output:
    # Square: area = 16, perimeter = 16

    # Test case for Circle
    circle = Circle(5)  # A circle with radius 5
    print(f"Circle: area = {circle.area():.2f}, perimeter = {circle.perimeter():.2f}")
    # Expected Output:
    # Circle: area = 78.54, perimeter = 31.42
    print(circle)  # Should print "Circle: radius = 5"

