#!/usr/bin/python3

'''grades a students scores'''
score = int(input("Enter your score please "))

if score >= 90:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")
