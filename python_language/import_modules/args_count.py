#!/usr/bin/python3

"""
Script that prints the number of arguments passed.
"""

import sys


def main():
    """
    Entry point
    """
    nums = len(sys.argv) - 1
    print(nums)

if __name__ == "__main__":
    main()
