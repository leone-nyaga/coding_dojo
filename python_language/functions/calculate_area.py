#!/usr/bin/python3

from typing import Union


def calculate_area(shape: str, dimensions: tuple) -> Union[float, str]:
    """
    Calculates area of either a circle or rectangle.

    Parameters:
    shape (str): Type of shape, 'rectangle, or 'circle'.
    dimensions (tuple):
        For a rectangle (length, width).
        For a circle (radius,).

    Returns:
    float: The area of either Rectangle or Circle.
    str: Error message.
    """
    if shape == "rectangle":
        if len(dimensions) != 2:
            return "Error: Invalid dimension for a Rectangle!"
        length, width = dimensions
        if not (
                isinstance(length, (int, float))
                and
                isinstance(width, (int, float))):
            return "Error: Dimensions must be numbers!"
        if length <= 0 or width <= 0:
            return "Error: Dimensions must be positive!"
        area = length * width
        return round(area, 2)

    elif shape == "circle":
        if len(dimensions) != 1:
            return "Error: Invalid dimension for a Circle!"
        (radius,) = dimensions
        if not (isinstance(radius, (int, float))):
            return "Error: Dimensions must be numbers!"

        if radius <= 0:
            return "Error: Dimensions must be positive!"
        area = 3.142 * radius * radius
        return round(area, 2)
    else:
        return "Shape not supported!"


def main():
    print(calculate_area("rectangle", (10, 5)))
    print(calculate_area("circle", (7,)))
    print(calculate_area("triangle", (5, 6)))
    print(calculate_area("rectangle", (10,)))
    print(calculate_area("circle", (3, 4)))


if __name__ == "__main__":
    main()
