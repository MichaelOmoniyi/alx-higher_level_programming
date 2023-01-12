#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        for i in row:
            new_row = []
            new_row.append(i ** 2)
        return (new_row)
        new_matrix.append(row)
    return (new_matrix)
