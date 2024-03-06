#!/usr/bin/python3

'''prints multiplcation table but in reverse'''

number = int(input("Enter a number: "))

count = 10
while count >= 1:
    product = number * count
    print(number, "*", count, "=", product)
    count -= 1 
