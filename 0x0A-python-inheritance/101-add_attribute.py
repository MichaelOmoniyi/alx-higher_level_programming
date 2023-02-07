#!/usr/bin/python3

"""This module that add attribute(s) to an object"""

def add_attribute(obj, att, value):
    """Adds attribute to a object"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
