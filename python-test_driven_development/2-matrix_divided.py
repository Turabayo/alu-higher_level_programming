#!/usr/bin/python3
# a function that divides all elements of a matrix
"""
    define function 'matrix_divided'
"""


def matrix_divided(matrix, div):
    """
        this function will devide the elements of a matrix
        by iterating over them using filter function
    """
    n_matrix = []
    x = 0
    n = len(matrix)
    if not (isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for
    row in matrix or not all(isinstance(element, int) or isinstance(element, float) for
    element in [num for num in matrix for num in row]))):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('each row of the matrix must have the same size')
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    while x < n:
        n_matrix.append(list(map(lambda y: round(y/div, 2), matrix[x])))
        x += 1
    return n_matrix
