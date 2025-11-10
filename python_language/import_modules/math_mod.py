#!/usr/bin/python3
import math

num = (int(input("Enter a number: ")))

if num < 0:
    print("Number must be greater than 0")
else:
    print(f"Square root: {math.sqrt(num):.2f}")
    print(f"Factorial: {math.factorial(num)}")
