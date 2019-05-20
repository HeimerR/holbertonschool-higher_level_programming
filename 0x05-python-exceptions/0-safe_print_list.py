#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end='')
    except Exception:
        print()
        return i
    else:
        print()
        return i + 1
