#!/usr/bin/python3

def safe_print_division(a, b):
    divide

    try:
        divide = a / b
    except (ValueError, ZeroDivisionError):
        print("Inside result: None")
    finally:
        print("Inside result: {:d}".format(divide))
    return (divide)
