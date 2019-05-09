#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        aux = a_dictionary.copy()
        for k, v in sorted(aux.items()):
            val = v * 2
            tuple_aux = {k: val}
            aux.update(tuple_aux)
        return aux
