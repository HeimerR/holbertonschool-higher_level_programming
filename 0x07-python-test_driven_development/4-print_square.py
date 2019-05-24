#!/usr/bin/python3
""" module witha a function that prints a square
"""


def print_square(size):
    """ prints a square with the character #

    Args:
        size (int): size of the sqaure
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size, end='')
        print()
