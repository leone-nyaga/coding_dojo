#!/usr/bin/python3

from mensuration import Mensuration

class Rectangle(Mensuration):

    def __init__(self, side._x: float, side._y: float) -> None:
    super().__init__(side._x, side._y)

    def area(self):
        return side._x * side._y

    def perimeter(self):
        return 2 * (self._x + self._y)

    def __str__(self):
        return f"Rectangle: side_x = {self.side_x}, side_y = {self.side_y}"
