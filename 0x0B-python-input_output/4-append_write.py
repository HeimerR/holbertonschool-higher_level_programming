#!/usr/bin/python3
"""module
append to a text file
"""


def append_write(filename="", text=""):
    """ appends a string to a text file (UTF8) and returns
        the number of characters added
    """
    with open(filename, encoding="utf-8", mode="a") as my_file:
        return my_file.write(text)
