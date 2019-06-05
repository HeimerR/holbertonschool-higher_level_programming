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
    for i in range(2:n):
        step = []
        step.insert(0, 1)
        for i in range(
        s = pascal[0][0]
        index = 1
        step.insert(index, s)
        pascal.append(step)
    return pascal
    #    for j in range(2:n):
     #       item = 
      #      step.insert(index, obj)
        
        
