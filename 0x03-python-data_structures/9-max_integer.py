#!/usr/bin/python3

def max_integer(my_list=[]):
    my_list.sort(reverse=True)
    if len(my_list) == 0:
        print("None")
    else:
        print("Max: {:d}".format(my_list))
