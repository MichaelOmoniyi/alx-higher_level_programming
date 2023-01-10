#!/usr/bin/python3

def max_integer(my_list=[]):
    my_list.sort(reverse=True)
    if len(my_list) == 0:
        return
    else:
        return (my_list[0])
