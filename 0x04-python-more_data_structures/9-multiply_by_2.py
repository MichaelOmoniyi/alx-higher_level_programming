#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()

    for i, j in new_dict.items:
        print("{:s}: {}".format(i, j ** 2))
        new_dict[i] = j
    return (new_dict)
