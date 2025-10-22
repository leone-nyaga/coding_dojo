#!/usr/bin/python3

from typing import Union

def get_grade(score: Union[int, float]) -> str:
    """
    Determines the letter grade for a given numeric score.

    Parameters:
    score (int or float): The student's score (0–100).

    Returns:
    str: A letter grade ('A', 'B', 'C', 'D', 'F') or
    an error message if the input is invalid.
    """
    if not isinstance(score, (int, float)):
        return "Error: score must be a number"

    if not (0 <= score <= 100):
        return "Error: score must be between 0 and 100"

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    print(get_grade(95))
    print(get_grade(75))
    print(get_grade(56))
    print(get_grade(120))
    print(get_grade("90"))


if __name__ == "__main__":
    main()
