#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if isinstance(key, str):
        del a_dictionary[key]
        return (a_dictionary)
    return (a_dictionary)
