#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Returns a new list with element of another list divided
    by a divisor

    Args:
        matrix (list): The list to be divided
        div (int) or (float): The divisor

    Raise:
        TypeError: If list does not contain only integers or floats
        TypeError: If row of the matrix have different sizes
        TypeError: If the divisor is not an integer or float
        ZeroDivisionError: If the divisor is zero

    Returns:
        A new list with elements divided
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(point, int) or isinstance(point, float))
                    for point in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix(list of lists)
                        of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
