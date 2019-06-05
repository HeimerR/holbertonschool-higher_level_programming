#!/usr/bin/python3
"""module
string to a text file
"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns
        the number of characters written
    """
    with open(filename, encoding="utf-8", mode="w") as my_file:
        return my_file.write(text)
