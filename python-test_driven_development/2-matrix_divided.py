#!/usr/bin/python3
"""Module that provides a function to divide a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div and return a new matrix.

    Each element is rounded to 2 decimal places.
    Raises TypeError if matrix is invalid or div is not a number.
    Raises ZeroDivisionError if div is 0.
    """
    if (not isinstance(matrix, list) or not matrix or
            any(not isinstance(row, list) or not row for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for el in row:
            value = round(el / div, 2)
            if value == 0:
                value = 0.0
            new_row.append(value)
        new_matrix.append(new_row)

    return new_matrix
