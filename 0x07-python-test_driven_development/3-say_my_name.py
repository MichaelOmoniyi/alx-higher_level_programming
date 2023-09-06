#!/usr/bin/python3
"""Defines a function that prints names"""

def say_my_name(first_name, last_name=""):
    """Prints first name and last name

    Args:
        first_name (str): First name
        last_name (str): Last name

    Raises:
        TypeError: If first_name or last_name is not a string

    Return:
        The first and last name
    """


    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
