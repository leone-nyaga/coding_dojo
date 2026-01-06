#!/usr/bin/python3
"""
This script prints the platform identifier of the current Python runtime.

It uses the built-in `sys` module to determine which operating system
Python is running on (e.g. 'linux', 'win32', 'darwin').

Intended to be run as a CLI script.
"""


import sys


def main():
    """
    Entry point

    Retrieves the platform information from sys.platform
    and prints it to standard output.
    """
    plat = sys.platform
    print(plat)


if __name__ == "__main__":
    main()
