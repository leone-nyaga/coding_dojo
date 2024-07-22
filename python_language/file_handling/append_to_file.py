#!/usr/bin/python3

"""function to append a line of text"""
def append_to_file(content, filename="python_file-handling.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content)

additional_content = "\n This is an additional line of text. \n"
append_to_file(additional_content)
