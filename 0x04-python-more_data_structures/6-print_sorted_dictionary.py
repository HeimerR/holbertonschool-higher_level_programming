#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        keys = sorted(a_dictionary.keys())
        for k in keys:
            print("{}: ".format(k), end='')
            print(a_dictionary.get(k))
