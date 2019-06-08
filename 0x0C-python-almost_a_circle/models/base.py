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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return []
        return json.dumps(list_dictionaries)
   
    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", encoding="utf-8", mode="w") as j_file:
            if list_objs != None:
                list_dict = [item.to_dictionary() for item in list_objs]
                j_file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None :
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as j_file:
                list_file = cls.from_json_string(j_file.read())
                return [cls.create(**obj) for obj in list_file]

        except IOError:
            return []

