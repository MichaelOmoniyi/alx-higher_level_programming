#!/usr/bin/python3

""" The Mylist class is inherited from a class list"""


class MyList(list):
    """ This class prints a sorted list"""
    def print_sorted(self):
        """ Prints a sorted list"""
        print(sorted(self))
