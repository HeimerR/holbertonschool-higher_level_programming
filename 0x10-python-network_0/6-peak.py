#!/usr/bin/python3
""" finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return (list_of_integers[0] if list_of_integers[0] >
                list_of_integers[1] else list_of_integers[1])
    left = find_peak(list_of_integers[0:int(len(list_of_integers) / 2)])
    right = find_peak(list_of_integers[int(len(list_of_integers) / 2):])
    return left if left > right else right
