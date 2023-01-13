#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    delete_key = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            delete_key.append(i)
    for j in delete_key:
        del a_dictionary[j]
    return a_dictionary
