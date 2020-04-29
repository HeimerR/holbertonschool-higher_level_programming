#!/usr/bin/python3
""" puzzle queen challenge
"""
from sys import argv, exit


def place(N, row, col, result):
    """ place queens recursively """
    if row == N:
        return result
    while col < N:
        if isvalid(row, col, result):
            result.append([row, col])
            result = place(N, row+1, 0, result)
            break
        col += 1
    if col == N:
        r, c = result.pop()
        result = place(N, r, c+1, result)
    return result


def isvalid(row, col, result):
    """ check if the position is valid """
    diag1 = [l[0]+l[1] for l in result]
    diag2 = [l[1]-l[0] for l in result]
    cols = [l[1] for l in result]
    rows = [l[0] for l in result]
    if row in rows or col in cols or row+col in diag1 or col-row in diag2:
        return False
    return True

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
    col = 0
    while col < N-1:
        result = []
        result = place(N, 0, col, result)
        print(result)
        col = result[0][1] + 1
