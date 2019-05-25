#!/usr/bin/python3
"""function that divides elements
   in a matrix
"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix

    Args:
        matrix (list): double list, elements int or float
        div (int/float): divisor
    """
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')
    if all(list(map(lambda x: x == list, list(map(type, matrix))))) is False:
        raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')
    if all(list(map(lambda x: all(list(map(lambda x:
       type(x) == int or type(x) == float, x))), matrix))) is False:
        raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')
    if all(list(map(lambda x: len(x) == len(matrix[0]), matrix))) is False:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    m = list(map(lambda x: list(map(lambda x: round(x / div, 2), x)), matrix))
    return m
