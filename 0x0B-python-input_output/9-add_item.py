#!/usr/bin/python3
"""module
adds all arguments to a Python list
"""
from sys import argv
import os
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    my_list = []
    if len(argv) > 1:
        for i in range(len(argv) - 1):
            my_list.append(argv[i + 1])
    if os.path.isfile(os.getcwd() + "/add_item.json"):
        json_list = load_from_json_file("add_item.json")
    else:
        with open("add_item.json", encoding="utf-8", mode="w"):
            json_list = []
    new_json = json_list + my_list
    save_to_json_file(new_json, "add_item.json")
