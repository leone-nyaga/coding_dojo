#!/usr/bin/python3

def display_student(name, age):
    """
    reassigns the calling function

    parameters:
    name(string): name of student
    age(int): age of student

    Returns:
    none
    """
    print(name, age)

display_student("Mary", 22)

show_student = display_student

show_student("Mary", 22)
