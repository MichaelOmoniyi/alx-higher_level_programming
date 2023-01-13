#!/usr/bin/python3

roman_to_int = __import__('12-roman_to_int').roman_to_int

string = "MDCXXXL"

roman_numeral = roman_to_int(string)
print("{:s} = {:d}".format(string, roman_numeral))
