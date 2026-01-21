#!/usr/bin/python3
"""
Module for matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.
    
    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix
        
    Returns:
        list of lists: Result of matrix multiplication
        
    Raises:
        TypeError: If matrices are not valid
        ValueError: If matrices cannot be multiplied or are empty
    """
    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    
    # Validate m_b  
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    # Validate elements in m_a
    row_len_a = None
    for row in m_a:
        if row_len_a is None:
            row_len_a = len(row)
        elif len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")
        
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    
    # Validate elements in m_b
    row_len_b = None
    for row in m_b:
        if row_len_b is None:
            row_len_b = len(row)
        elif len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")
        
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    
    # Check if matrices can be multiplied
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(row_len_b)] for _ in range(len(m_a))]
    
    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(row_len_b):
            for k in range(row_len_a):
                result[i][j] += m_a[i][k] * m_b[k][j]
    
    return result
