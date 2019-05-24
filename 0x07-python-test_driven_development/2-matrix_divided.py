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
    if type(div) is not int and  type(div) is not float:
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    len_rows = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')
        else:
            len_rows.append(len(row))
        for item in row:
            if type(item) is not int and  type(item) is not float:
                raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')
    if all(x == len_rows[0] for x in len_rows) is False:
        raise TypeError('Each row of the matrix must have the same size')
    new_matrix = list(map(lambda x: list(map(lambda x: round(x / div, 2), x)), matrix))
    return new_matrix
                

