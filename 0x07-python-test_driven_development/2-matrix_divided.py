#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Division of the matrix.

    Checks if the matrix is a list and its elements are integers or floats,
    otherwise raises a TypeError.
    Checks the length of the matrix; if it is empty, raises a TypeError.
    Checks if div is an int or float; otherwise raises a TypeError.
    Checks if div is not equal to 0; otherwise raises a ZeroDivisionError.
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(elements, int) or
                 isinstance(elements, float)for elements in
                 [numbers for row in matrix for numbers in row]))):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, float) or isinstance(div, int)):
        raise TypeError("div must be a number")
    return [[round(element / div, 2) for element in row] for row in matrix]
