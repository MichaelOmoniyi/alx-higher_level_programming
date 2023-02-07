#!/usr/bin/python3

"""This module defines a file-appending function"""


def write_file(filename="", text=""):
    """This function appends a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
