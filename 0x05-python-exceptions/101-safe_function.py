#!/usr/bin/python3
import sys

"""executes a funtion

Args:
    fct (funtcion): The function to be executed
    args (arguments): Arguments to be passed into function

Returns:
    The result of the function, otherwise, None
"""


def safe_function(fct, *args):
    try:
        result = fct(args)
    except Exception in e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return result
