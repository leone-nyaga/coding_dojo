#!/usr/bin/python3

'''prints factors of a positive integer using a while loop'''
# Take user input for a positive integer
number = int(input("Enter a positive integer: "))

# Validate input
while number <= 0:
    print("Invalid input. Please enter a positive integer.")
    number = int(input("Enter a positive integer: "))

# Initialize a variable for the factor
factor = 1

# Print factors using a while loop
print(f"The factors of {number} are:")

while factor <= number:
    if number % factor == 0:
        print(factor)
        factor += 1

