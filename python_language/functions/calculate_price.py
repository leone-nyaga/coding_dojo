#!/usr/bin/python3

from typing import Union


def calculate_price(price: Union[int, float], discount: float = 10, tax: float = 10) -> Union[float, str]:
    """
    Calculates the final price of an item after applying a discount and tax.

    Parameters:
    price (int or float): The original price of the item (must be positive).
    discount (float, optional): The discount percentage to apply (default is 10%).
    tax (float, optional): The tax percentage to apply (default is 5%).

    Returns:
    float: The final price rounded to 2 decimal places.
    str: An error message if inputs are invalid.
    """
    # Validate data types
    if not all(isinstance(x, (int, float)) for x in [price, discount, tax]):
        return "Error: all inputs must be numbers"

    # Validate value ranges
    if price <= 0:
        return "Error: price must be positive"
    if not (0 <= discount <= 100):
        return "Error: discount must be between 0 and 100"
    if not (0 <= tax <= 100):
        return "Error: tax must be between 0 and 100"

    # Apply discount
    discounted_price = price * (1 - discount / 100)

    # Apply tax on discounted price
    final_price = discounted_price * (1 + tax / 100)

    return round(final_price, 2)


def main():
    print(calculate_price(100))
    print(calculate_price(200, 20))
    print(calculate_price(150, 10, 10))
    print(calculate_price(-50))
    print(calculate_price(100, "ten"))


if __name__ == "__main__":
    main()
