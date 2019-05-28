#!/usr/bin/python3
""" puzzle queen challenge
"""
from sys import argv, exit


if __name__ == "__main__":
    length = len(argv)
    if length != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    N = int(argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)
    result = [[0, 0]]
    for x in range(N):
        for y in range(N):
            if all(list(map(lambda x: x != 3, [result[x][0]
                   for x in range(len(result))]))) is False:
                break
