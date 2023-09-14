#!/usr/bin/python3
"""Defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """The function returns a list of lists of
        integers representing the Pascal’s triangle of n

    Args:
        n (int): The Pascal number
    """

    triangle = []
    if n == 0:
        return triangle
    else:
        row = 0
        while row < n:
            row_list = []
            value = 1
            if row == 0:
                row_list.append(value)
                triangle.append(row_list)
            elif row == 1:
                row_list.append(value)
                row_list.append(value)
                triangle.append(row_list)
            else:
                for num in range(row):
                    if num == 0:
                        row_list.append(value)
                    else:
                        value = (triangle[row - 1][num]) \
                            + (triangle[row - 1][num - 1])
                        row_list.append(value)
                row_list.append(1)
                triangle.append(row_list)
            row += 1
        return triangle
