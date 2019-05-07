#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        local = my_list.copy()
        local.reverse()
        for i in range(len(local)):
            print("{:d}".format(local[i]))
