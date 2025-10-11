#!/usr/bin/python3

score = int(input("Enter score (0–100): "))

if 0 <= score <= 100:

    if 90 <= score <= 100:
        print("A")
    elif 80 <= score < 90:
        print("B")
    elif 70 <= score < 80:
        print("C")
    elif 60 <= score < 70:
        print("D")
    else:
        print("F")
else:
    print("Invalid input. Please enter a number between 0 and 100.")
