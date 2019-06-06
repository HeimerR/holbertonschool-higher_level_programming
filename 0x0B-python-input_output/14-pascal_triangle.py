#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    pascal = []
    if n <= 0:
        return pascal
    pascal = [[1]]
    if n == 1:
        return pascal
    for j in range(1, n):
        for i in range(1, n):
            step = []
            step.insert(0, 1)
            for k in range(len(pascal[j - 1]) - 1):
                v = pascal[j - 1][k - 1] + pascal[j - 1][k]
                step.insert(k, v)
            step.insert(-1, 1)
        pascal.append(step)
    pascal1 = list(map(lambda x: [1] + x, pascal))
    for sub in pascal1:
        sub.pop(-1)
    return pascal1
