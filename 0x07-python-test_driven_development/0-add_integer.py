#!/usr/bin/python3
""" this modulo has a function that adds 2 intergers
    you can test it using testfile
    included in /test//0-add_integer.txt

"""


def add_integer(a, b=98):
    """ adds 2 intergers, float casted to intgers
    Args:
        a (int): number one
        b (int): number two
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
