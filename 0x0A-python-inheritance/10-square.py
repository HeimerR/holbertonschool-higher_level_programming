#!/usr/bin/python3
""" module square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """ init rectangle """
        Rectangle.__init__(self, size, size)
        self.__size = size
