#!/usr/bin/python3

from mensuration import Mensuration

class Rectangle(Mensuration):

    def __init__(self, side_x: float, side_y: float) -> None:
        super().__init__(side_x, side_y)

    def area(self):
        return self.side_x * self.side_y

    def perimeter(self):
        return 2 * (self.side_x + self.side_y)

    def __str__(self):
        return f"Rectangle: side_x = {self.side_x}, side_y = {self.side_y}"
