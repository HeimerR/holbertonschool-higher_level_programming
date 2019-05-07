#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        aux = my_list.copy()
        for i in range(len(my_list)):
            aux[i] = my_list[i] % 2 == 0
        return aux
