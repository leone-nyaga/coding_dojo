#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Return the element at a given index in a list.
    Returns None if the index is out of bounds.
    """
    if idx < 0 or idx > len(my_list):
        return None

    return my_list[idx]
