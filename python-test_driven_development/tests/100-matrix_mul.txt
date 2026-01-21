Test cases for matrix_mul function

>>> matrix_mul = __import__('100-matrix_mul').matrix_mul

Test 1: Basic 2x2 matrix multiplication
>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[7, 10], [15, 22]]

Test 2: 1x2 * 2x2 matrix
>>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
[[13, 16]]

Test 3: 3x2 * 2x3 matrix
>>> matrix_mul([[1, 2], [3, 4], [5, 6]], [[1, 2, 3], [4, 5, 6]])
[[9, 12, 15], [19, 26, 33], [29, 40, 51]]

Test 4: Matrix with zeros
>>> matrix_mul([[0, 0], [0, 0]], [[1, 2], [3, 4]])
[[0, 0], [0, 0]]

Test 5: Matrix with floats
>>> matrix_mul([[1.5, 2.5], [3.5, 4.5]], [[2, 0], [0, 2]])
[[3.0, 5.0], [7.0, 9.0]]

Test 6: Error - m_a not a list
>>> matrix_mul("not a list", [[1, 2], [3, 4]])
Traceback (most recent call last):
    ...
TypeError: m_a must be a list

Test 7: Error - m_b not a list
>>> matrix_mul([[1, 2], [3, 4]], "not a list")
Traceback (most recent call last):
    ...
TypeError: m_b must be a list

Test 8: Error - m_a not list of lists
>>> matrix_mul([1, 2, 3], [[1, 2], [3, 4]])
Traceback (most recent call last):
    ...
TypeError: m_a must be a list of lists

Test 9: Error - m_b not list of lists
>>> matrix_mul([[1, 2], [3, 4]], [1, 2, 3])
Traceback (most recent call last):
    ...
TypeError: m_b must be a list of lists

Test 10: Error - m_a empty
>>> matrix_mul([], [[1, 2], [3, 4]])
Traceback (most recent call last):
    ...
ValueError: m_a can't be empty

Test 11: Error - m_b empty
>>> matrix_mul([[1, 2], [3, 4]], [])
Traceback (most recent call last):
    ...
ValueError: m_b can't be empty

Test 12: Error - m_a empty nested
>>> matrix_mul([[]], [[1, 2], [3, 4]])
Traceback (most recent call last):
    ...
ValueError: m_a can't be empty

Test 13: Error - m_b empty nested
>>> matrix_mul([[1, 2], [3, 4]], [[]])
Traceback (most recent call last):
    ...
ValueError: m_b can't be empty

Test 14: Error - non-numeric element in m_a
>>> matrix_mul([[1, 'a'], [3, 4]], [[1, 2], [3, 4]])
Traceback (most recent call last):
    ...
TypeError: m_a should contain only integers or floats

Test 15: Error - non-numeric element in m_b
>>> matrix_mul([[1, 2], [3, 4]], [[1, 'b'], [3, 4]])
Traceback (most recent call last):
    ...
TypeError: m_b should contain only integers or floats

Test 16: Error - rows not same size in m_a
>>> matrix_mul([[1, 2], [3, 4, 5]], [[1, 2], [3, 4]])
Traceback (most recent call last):
    ...
TypeError: each row of m_a must be of the same size

Test 17: Error - rows not same size in m_b
>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4, 5]])
Traceback (most recent call last):
    ...
TypeError: each row of m_b must be of the same size

Test 18: Error - matrices cannot be multiplied
>>> matrix_mul([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4]])
Traceback (most recent call last):
    ...
ValueError: m_a and m_b can't be multiplied

Test 19: 1x1 matrix multiplication
>>> matrix_mul([[5]], [[6]])
[[30]]

Test 20: 2x1 * 1x2 matrix
>>> matrix_mul([[1], [2]], [[3, 4]])
[[3, 4], [6, 8]]

Test 21: Identity matrix multiplication
>>> matrix_mul([[1, 0], [0, 1]], [[5, 6], [7, 8]])
[[5, 6], [7, 8]]

Test 22: Negative numbers
>>> matrix_mul([[-1, -2], [-3, -4]], [[1, 2], [3, 4]])
[[-7, -10], [-15, -22]]

Test 23: Mixed positive and negative
>>> matrix_mul([[1, -2], [-3, 4]], [[-5, 6], [7, -8]])
[[-19, 22], [43, -50]]
