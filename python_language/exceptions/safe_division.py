#!/usr/bin/env python3


def safe_divide(num: int) -> float:
    """
    Divides 10 by a given number


    Args:
        num (int): A positive integer.


    Returns:
        Float: The result of 10 divided by a given number.

    """
    return 10 / num


def main() -> None:
    """
    Main function to interact with the user.

    Continuously prompts user to type an integer.
    Validates the input, handles errors, and prints the division result.
    The user can enter 'q' to quit the program.
    """
    while True:
        user_input = input("Please enter a number: ")

        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        try:
            number = int(user_input)
        except ValueError:
            print("Number must be an integer!")
            continue

        if number <= 0:
            print("Number must be greater than zero")
            continue

        try:
            result = safe_divide(number)
        except ZeroDivisionError:
            print("Number must be greater than zero!")
            continue
        else:
            print(result)


if __name__ == '__main__':
    main()
