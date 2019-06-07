#!/usr/bin/python3
"""
Module base
"""


class Base:
    """class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """id"""
        if id != None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
