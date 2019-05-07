#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        local = my_list.copy()
        if idx < 0 or idx >= len(my_list):
            return local
        else:
            local[idx] = element
        return local
