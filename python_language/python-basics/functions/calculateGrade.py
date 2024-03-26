#!/usr/bin/python3

def find_averageMarks(marks):
    """
    Calculates the average marks in a list

    Parameters:
    marks(list): a list containing marks

    Returns:
    average marks
    """
    sum_of_marks = sum(marks)
    number_of_marks = len(marks)

    average_marks = sum_of_marks/number_of_marks
    return(average_marks)

def compute_grade(average_marks):
    """
    Finds the Grade scored.

    Parameters:
    average_marks: Average marks obtained.

    Returns:
    str
    """
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    elif average_marks >= 40:
        grade = 'D'
    else:
        grade = 'F'

    return grade

marks = [80, 99, 68, 91, 87, 75, 85]
average_marks = find_averageMarks(marks)
grade = compute_grade(average_marks)

print(f"Your average marks is {average_marks:.2f}")
print(f"Your grade is {grade}")
