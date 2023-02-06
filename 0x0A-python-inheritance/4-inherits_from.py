#!/usr/bin/python3

""" This module check if an object is an instance of an inherited class"""


def inherits_from(obj, a_class):
    """ Returns True if obj is an instance of class a_class,
    and False if otherwise"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
