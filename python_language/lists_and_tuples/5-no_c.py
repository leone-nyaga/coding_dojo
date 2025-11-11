#!/usr/bin/python3

def no_c(my_string):
    """
    function that removes all characters c and C from a string
    """
    new_string = ""
    
    for character in my_string: 
        if character != "C" and character != "c":
            new_string += character

    return new_string

