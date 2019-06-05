#!/usr/bin/python3
"""  number of lines of a text file
"""


def number_of_lines(filename=""):
    """t returns the number of lines of a text file"""
    with open(filename, encoding="utf-8") as my_file:
        return len(my_file.readlines())
