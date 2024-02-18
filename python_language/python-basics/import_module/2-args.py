#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    y = len(argv) - 1
    if y == 0:
        print("0 arguments.")
    elif y == 1:
        print("1 argument.")
    else:
        print(f"{y} arguments.")

    if (y > 0):
        for i in range(1, y + 1):
            print(f"Argument {i}: {argv[i]}") 
