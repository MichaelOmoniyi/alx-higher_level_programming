#!/usr/bin/python3

"""print and integer with "{:d}".format()

Args:
    value: integer to be printed

Returns:
    True, if value has been correctly printed
    False, if otherwise
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
