#!/usr/bin/python3

from typing import Union


def convert_temperature(
        temp: Union[int, float],
        from_unit: str, to_unit: str
        ) -> Union[float, str]:
    """
    Converts a temperature from one unit to another (Celsius, Fahrenheit, Kelvin).
    
    Parameters:
    temp (int or float): The temperature value to convert.
    from_unit (str): The unit of the input temperature ('C', 'F', or 'K').
    to_unit (str): The unit to convert to ('C', 'F', or 'K').

    Returns:
    float: The converted temperature, rounded to 2 decimal places.
    str: Error message if inputs are invalid.
    """
    
    # Normalize unit inputs to uppercase
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # List of valid units
    valid_units = ["C", "F", "K"]

    # Validate units
    if from_unit not in valid_units or to_unit not in valid_units:
        return "Error: invalid temperature unit"

    # Check for temperature below absolute zero
    if from_unit == "C" and temp < -273.15:
        return "Error: temperature below absolute zero in Celsius"
    if from_unit == "F" and temp < -459.67:
        return "Error: temperature below absolute zero in Fahrenheit"
    if from_unit == "K" and temp < 0:
        return "Error: temperature below absolute zero in Kelvin"

    # Step 1: Convert input temperature to Celsius
    if from_unit == "C":
        temp_celsius = temp
    elif from_unit == "F":
        temp_celsius = (temp - 32) * 5 / 9
    elif from_unit == "K":
        temp_celsius = temp - 273.15

    # Step 2: Convert from Celsius to target unit
    if to_unit == "C":
        converted = temp_celsius
    elif to_unit == "F":
        converted = temp_celsius * 9 / 5 + 32
    elif to_unit == "K":
        converted = temp_celsius + 273.15

    # Step 3: Return rounded result
    return round(converted, 2)


def main():
    print(convert_temperature(100, "C", "F"))
    print(convert_temperature(32, "F", "C"))
    print(convert_temperature(0, "K", "C"))
    print(convert_temperature(-500, "F", "C"))
    print(convert_temperature(25, "X", "C"))


if __name__ == "__main__":
    main()
