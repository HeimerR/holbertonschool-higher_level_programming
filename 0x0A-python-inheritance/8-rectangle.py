#!/usr/bin/python3
""" module subclass rectangle
"""


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        integer_validator(self)
        self.__height = height
        self.__width = width
