#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="")
        return True
    except (ValueError):
        return False
        raise ValueError
