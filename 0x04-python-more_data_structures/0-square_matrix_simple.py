#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[row[i]**2 for i in range(len(matrix[0]))] for row in matrix]
