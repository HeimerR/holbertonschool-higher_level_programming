#!/usr/bin/python3
""" finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    peak = list_of_integers[0]
    for n in list_of_integers:
        if n > peak:
            peak = n
    return peak
