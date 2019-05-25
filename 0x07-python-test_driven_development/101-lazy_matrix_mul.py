#!/usr/bin/python3
""" module to multiply 2 matrices
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiply 2 matrices using numpy
    """
    return numpy.matmul(m_a, m_b)
