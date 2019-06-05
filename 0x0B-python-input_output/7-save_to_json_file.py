#!/usr/bin/python3
"""module
writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation"""
    with open(filename, encoding="utf-8", mode="w") as json_file:
        json_file.write(json.dumps(my_obj))
