#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        aux = a_dictionary.copy()
        for item in aux:
            val = aux[item] * 2
            tuple_aux = {item: val}
            aux.update(tuple_aux)
        return aux
