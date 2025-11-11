#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """
    Print all items of a list.

    Args:
        my_list: List of integers to print.

    Returns:
        None
    """
    if my_list is None:
        return []

    for item in range(len(my_list)):
        print("{}".format(item))
