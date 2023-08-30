#!/usr/bin/python3

"""Print x elements of a list.

Args:
    my_list(list): The list of whose element to be printed.
    x (int): The number of element to be printed.

Returns:
    The number of element printed.
"""


def safe_print_list(my_list=[], x=0):
    length = 0

    for i in range(0, x):
        try:
            print(f"{my_list[i]}", end="")
            length += 1
        except IndexError:
            print("\n{x} greater than the length of my_list")
            break
    print("")
    return (length)
