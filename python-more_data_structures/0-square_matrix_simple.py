#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return a new matrix with squared values."""
    return [[value ** 2 for value in row] for row in matrix]
