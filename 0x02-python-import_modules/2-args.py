#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    if length < 2:
        print('0 arguments.')
    elif length == 2:
        print('1 argument:')
    else:
        print('{:d} arguments:'.format(length - 1))
    for i in range(1, length):
        print('{:d}: {}'.format(i, argv[i]))
