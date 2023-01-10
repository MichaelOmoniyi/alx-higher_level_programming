#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > len(tuple_b):
        len_tuple = len(tuple_a)
    else:
        len_tuple = len(tuple_b)

    for i in range(len(len_tuple)):
        if len(tuple_a) < 2 and i >= 2:
            list_tuple = 0, tuple_b[i]
            return (list_tuple)
        elif len(tuple_b) < 2 and i >= 2:
            list_tuple = tuple_b[i], 0
            return (list_tuple)
        else:
            list_tuple = tuple_a[i], tuple_b[i]
            return (list_tuple)
