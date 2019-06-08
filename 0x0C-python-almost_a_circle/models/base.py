#!/usr/bin/python3
"""
Module base
"""
import json


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

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return []
        return json.dumps(list_dictionaries)
   
    @classmethod
    def save_to_file(cls, list_objs):
        print(cls.__name__)
