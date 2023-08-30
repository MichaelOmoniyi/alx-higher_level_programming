#!/usr/bin/python3

"""divides 2 integers
Args:
    a (int): integer to be divided
    b (int): integer

Returns:
    The value of the division
"""


def safe_print_division(a, b):
    try:
        divide = a / b
    except (TypeError, ZeroDivisionError):
        divide = None
    finally:
        print("Inside result: {}".format(divide))
    return (divide)
