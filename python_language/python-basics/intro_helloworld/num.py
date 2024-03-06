#!/usr/bin/python3

"""
Ask a user to input two values and store them in variables num1 and num2.
"""

# Ask a user to input two values and store them in variables num1 and num2
num1, num2 = input("Enter 2 numbers separated by a space: ").split()

# Convert strings to integers
num1 = int(num1)
num2 = int(num2)

"""
Perform arithmetic operations on the numbers and display the results.
"""

# Add the values of two numbers
addition_result = num1 + num2
print("Addition result:", addition_result)

# Subtract the values of two numbers
subtraction_result = num1 - num2
print("Subtraction result:", subtraction_result)

# Divide the values of two numbers
division_result = num1 / num2
print("Division result:", division_result)

# Multiply the values of two numbers
multiplication_result = num1 * num2
print("Multiplication result:", multiplication_result)

# Calculate the modulus of two numbers
modulus_result = num1 % num2
print("Modulus result:", modulus_result)
