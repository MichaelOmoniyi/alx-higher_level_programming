#!/usr/bin/python3
import sys

"""prints an integer

Args:
    value: integer to be printed

Returns:
    True, if successful
    False, if not
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
        print("Exception: {}".format((sys.exc_info()[1]), file=sys.stderr))
