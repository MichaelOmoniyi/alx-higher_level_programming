#!/usr/bin/pyton3

""" This module defines a text reading file"""


def read_file(filename=""):
    """This function reads a textfile and print to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
