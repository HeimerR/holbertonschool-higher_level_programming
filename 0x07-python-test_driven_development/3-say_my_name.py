#!/usr/bin/python3
"""module with function print name
"""


def say_my_name(first_name, last_name=""):
    """ function that prints
        My name is <first name> <last name>
    Args:
        first_name (str): first name to print
        last_name (str): last name to print
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
