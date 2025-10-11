#!/usr/bin/python3

char = input("Enter a vowel, ")

if len(char) == 1 and char.isalpha():
    if char.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid!")
