#!/usr/bin/python3
""" module
"""


class Student:
    """ class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) is list and
           all(list(map(lambda x: type(x) == str, attrs)))):
            my_dict = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    value = getattr(self, attr)
                    my_dict.update({attr: value})
            return my_dict
        else:
            return self.__dict__
