#!/usr/bin/python3

secret = 7

user_secret = int(input("Enter secret number, "))

while user_secret != secret:
    if user_secret > secret:
        print("Too High")
    elif user_secret < secret:
        print("Too Low")
    
    user_secret = int(input("Try again: "))
    
print("Correct Quess")
