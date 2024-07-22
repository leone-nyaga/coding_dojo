#!/usr/bin/python3

"""python function to create and write a Python_file-handling.txt file"""

def create_and_write_file():
    content = """\
            Python File Handling
            ----------------------
            This file will serve as a reference for discussing various file handling concepts in Python.

            Topics covered include:
            1. Opening and Closing a file.
            2. Reading from files.
            3. Writing to a file.
            4. Appending to a file.
            5. Working with binary files.
            6. Handling Exceptions
            7. Reading and writing large files

            Let's get started!
            """

    with open("python_file-handling.txt", "w", encoding="utf-8") as file:
        file.write(content)

create_and_write_file()
