#!/usr/bin/python3

num1 = int(input("Enter number, "))
num2 = int(input("Enter number, "))

operator = input("Enter operation (+, -, *, /), ")

if operator == '+':
    result = num1 + num2
    print(f"Result {result}")

elif operator == '-':
    result = num1 - num2
    print(f"Result {result}")

elif operator == '*':
    result = num1 * num2
    print(f"Result {result}")

elif operator == '/':

    if num2 != 0:
        result = num1 / num2
        print(f"Result {result}")
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operator")
