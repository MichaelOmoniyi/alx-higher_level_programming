#!/usr/bin/python3
"""Defines an addition function"""

def add_integer(a, b=98):
    """Adds two integers together

    Argv:
        a (int): integer to be added
        b (int): integer to be added

    Raises:
        TypeError: If a or b is a non-integer or non-float
    Returns:
        The addition of the a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
