#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        localstr = my_string.translate({ord('c'): None})
        localstr = localstr.translate({ord('C'): None})
        return localstr
