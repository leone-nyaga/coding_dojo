#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific index.

    If idx is negative or out of range, do nothing and return the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
