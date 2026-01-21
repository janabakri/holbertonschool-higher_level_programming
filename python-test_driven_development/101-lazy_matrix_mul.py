#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    """
    # First validate with custom checks to match expected error messages
    if not isinstance(m_a, list):
        if isinstance(m_a, (int, float, str)):
            raise TypeError("Scalar operands are not allowed, use '*' instead")
        else:
            raise TypeError("m_a must be a list")
    
    if not isinstance(m_b, list):
        if isinstance(m_b, (int, float, str)):
            raise TypeError("Scalar operands are not allowed, use '*' instead")
        else:
            raise TypeError("m_b must be a list")
    
    # Rest of validation remains the same
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    row_len_a = None
    for row in m_a:
        if row_len_a is None:
            row_len_a = len(row)
        elif len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    
    row_len_b = None
    for row in m_b:
        if row_len_b is None:
            row_len_b = len(row)
        elif len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    try:
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        result = np.matmul(np_a, np_b)
        return result
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
