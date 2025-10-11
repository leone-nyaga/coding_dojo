#!/usr/bin/python3

multiple: int = int(input("Enter number, "))
start: int = 1
end: int = 12

while start <= end:
    result = start * multiple
    print(f"{start} X {multiple} = {result}")
    start += 1
