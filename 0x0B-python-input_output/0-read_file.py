#!/usr/bin/python3

""" This module defines a text reading file"""


def read_file(filename=""):
    """This function reads a textfile and print to stdout"""

    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
