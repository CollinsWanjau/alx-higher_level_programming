#!/usr/bin/python3
"""
Defines a matrix division function
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix (list): A list of lists of ints or floats
        div (int/float): The divisor
    Raises:
        TypeError: if matrix is not a matrix(list of lists)
        TypeError: if row of matrix is not same size
        TypeError: if div is not a number(int or float)
        ZeroDivisionError: div must not be 0
    Returns:
        A new matrix representing the result of the division
    """
    if matrix is None or len(matrix)==0 or not all(isinstance(row, list) for row in matrix) or not all(isinstance(elem, (int, float))
                for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return (list(map(lambda x: list(map(lambda y: round(y/div, 2), x)), matrix)))
    
