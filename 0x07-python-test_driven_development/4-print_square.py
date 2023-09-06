#!/usr/bin/python3
"""Defines a print_square function"""


def print_square(size):
    """The function prints squares

    Args:
        size (int): The size of the square

    Raises:
        TypeError: If size in not an integer.
        TypeError: If size is a float and is less than zero
        ValueError: If size is less than zero

    Return:
        A # square with the specified size
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        pass
    else:
        for y in range(size):
            for x in range(size):
                print("#", end="")
            print()
