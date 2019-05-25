#!/usr/bin/python3
""" Module mul matrix
"""


def matrix_mul(m_a, m_b):
    """t multiplies 2 matrices
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    if all(list(map(lambda x: x == list, list(map(type, m_a))))) is False:
        raise TypeError('m_a must be a list of lists')
    if all(list(map(lambda x: x == list, list(map(type, m_b))))) is False:
        raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if all(list(map(lambda x: x != 0, list(map(len, m_a))))) is False:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if all(list(map(lambda x: x != 0, list(map(len, m_b))))) is False:
        raise ValueError("m_b can't be empty")
    if all(list(map(lambda x: all(list(map(lambda x:
       type(x) == int or type(x) == float, x))), m_a))) is False:
        raise TypeError('m_a should contain only integers or floats')
    if all(list(map(lambda x: all(list(map(lambda x:
       type(x) == int or type(x) == float, x))), m_b))) is False:
        raise TypeError('m_b should contain only integers or floats')
    if all(list(map(lambda x: len(x) == len(m_a[0]), m_a))) is False:
        raise TypeError("each row of m_a must should be of the same size")
    if all(list(map(lambda x: len(x) == len(m_b[0]), m_b))) is False:
        raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    mul = []
    for i in range(len(m_a)):
        mul_row = []
        for j in range(len(m_b[0])):
            item = 0
            for k in range(len(m_b)):
                item += m_a[i][k] * m_b[k][j]
            mul_row.append(item)
        mul.append(mul_row)
    return mul
