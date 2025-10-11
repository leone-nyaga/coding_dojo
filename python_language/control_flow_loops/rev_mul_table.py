#!/usr/bin/python3

multiple: int = int(input("Enter the number for the table, "))
start: int = 1
end: int =  12

while end >= start:
    result = end * multiple
    print(f"{end} x {multiple} = {result}")
    end -= 1
