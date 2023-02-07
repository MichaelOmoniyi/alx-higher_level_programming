#!/usr/bin/pyton3

""" This module reads a textfile and print to stdout input"""


def read_file(filename=""):
    """This function reads a textfile"""

    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
