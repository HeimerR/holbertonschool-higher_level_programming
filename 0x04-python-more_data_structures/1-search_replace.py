#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        return [replace if item is search else item for item in my_list]
