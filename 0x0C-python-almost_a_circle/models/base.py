#!/usr/bin/python3
"""
Module base
"""
import json
import csv



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
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open(cls.__name__ + ".csv", mode="w") as f_csv:
            if list_objs != None:
                values = [ 'id', 'width', 'height', 'size', 'x', 'y'] 
                list_dict = [item.to_dictionary() for item in list_objs]
                values_header = filter(lambda y: y in list_dict[0], values)
                writer = csv.DictWriter(f_csv, fieldnames=list(values_header))
                writer.writeheader()
                for line in list_dict:
                    writer.writerow(line)

    @classmethod
    def load_from_file_csv(cls):
        try:
            with open(cls.__name__ + ".csv") as j_file:
                reader = csv.DictReader(j_file)
                list_dicts = []
                for row in reader:
                    for keys in row:
                        row[keys] = int(row[keys])
                    list_dicts.append(row)
                list_objs = [cls.create(**obj) for obj in list_dicts]
                return list_objs

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):

