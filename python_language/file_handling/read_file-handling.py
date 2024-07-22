"""function to read content from python_file-handling.py file"""

def read_file(filename="python_file-handling.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())

read_file()
