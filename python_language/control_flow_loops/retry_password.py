#!/usr/bin/python3

password: str = "python123"
user_password: str = input("Enter password, ")
attempts: int = 0
max_attempts: int = 3

while user_password != password and attempts < max_attempts - 1:
    attempts += 1
    print("Oops, Try Again")
    user_password: str = input("Enter password, ")

if user_password == password:
    print("Access granted!")
else:
    print("Access Denied")
