#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided
matrix = [
    [4.2, 8.4, 2.2],
    [10.8, 12.6, 6.2]
]
print(type(matrix))
print(matrix_divided(matrix, 3))
print(matrix)


