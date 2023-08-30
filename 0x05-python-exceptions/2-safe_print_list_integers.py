#!/usr/bin/python3

"""Prints the first x elements of a list and only integers

Args:
    my_list (list): List whose element is to be printed
    x (int): Number of elements to be printed

Returns:
    The real number of elements printed
"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return (count)
