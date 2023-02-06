#!/usr/bin/python3

""" This module checks for instance of an object"""


def is_kind_of_class(obj, a_class):
    """ The function returns True if obj is an instance of a_class,
    and False, if otherwise"""

    if not isinstance(obj, a_class):
        return False
    else:
        return True
