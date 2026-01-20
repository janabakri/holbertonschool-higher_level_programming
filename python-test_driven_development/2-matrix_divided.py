#!/usr/bin/python3
"""
This module contains the matrix_divided function
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats
        div: A number (integer or float) to divide by

    Returns:
        A new matrix with all elements divided by div,
        rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows have different sizes, or if div is not a number
        ZeroDivisionError: If div is zero
    """
    # Check if matrix is a list
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Check if all rows are lists and have same length
    row_length = None
    for row in matrix:
        # Check if row is a list
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        # Check if all elements are integers or floats
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

        # Check if all rows have same size
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements and round to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = element / div
            # Round to 2 decimal places
            rounded = round(result, 2)
            # Handle special case for infinity and -0.0
            if rounded == -0.0:
                rounded = 0.0
            new_row.append(rounded)
        new_matrix.append(new_row)

    return new_matrix
