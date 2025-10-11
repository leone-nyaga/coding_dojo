#!/usr/bin/python3

total: int = 0

num: int = int(input("Enter number above zero, "))

while num != 0:
    total += num
    print(f"{total}")
    num = int(input("Enter a number (0 to stop): "))

print(f"Overall Total sum {total}")
