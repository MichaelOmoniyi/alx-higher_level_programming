#!/usr/bin/python3

def safe_print_division(a, b):
    divide

    try:
        divide = a / b
    except (ValueError, ZeroDivisionError):
        divide = None
    finally:
        print("Inside result: {}".format(divide))
    return (divide)
