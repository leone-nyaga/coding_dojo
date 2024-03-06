#!/usr/bin/python3

if __name__ == "__main__":

    from math_operations import add, subtract, multiply, divide

    a = 10
    b = 5

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
