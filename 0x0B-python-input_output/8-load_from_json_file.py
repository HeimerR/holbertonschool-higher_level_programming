#!/usr/bin/python3
"""
Object from a “JSON file
"""
import json


def load_from_json_file(filename):
    with open(filename, encoding="utf-8") as json_file:
        return json.load(json_file)
