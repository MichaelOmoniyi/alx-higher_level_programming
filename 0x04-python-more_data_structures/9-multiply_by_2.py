#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()

    for i in new_dict:
        for j in new_dict.values():
            new_dict[i] = j ** 2
    return (new_dict)
