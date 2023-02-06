#!/usr/bin/python3

""" The Mylist class is inherited from a class list"""
class Mylist(list):
    """ This class prints a sorted list"""

    def print_sorted(self):
        list.sort()
        print(list)
