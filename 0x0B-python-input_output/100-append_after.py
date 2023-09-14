#!/usr/bin/python3
"""Defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line
        containing a specific string

    Args:
        filename (str): The name of the file
        search_string (str): The string to be searched for in the file
        new_string (str): The string to be appended to the line with
                            the searched string.
    """

    text = ""
    with open(filename) as fileRead:
        for line in fileRead:
            text += line

            if search_string in line:
                text += new_string

    with open(filename, mode="w", encoding="utf-8") as fileWrite:
        fileWrite.write(text)
