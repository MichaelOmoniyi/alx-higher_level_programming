#!/usr/bin/python3

def roman_to_int(roman_string):
    romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0

    if not roman_string or type(roman_string) != str:
        return 0
    for i in range(len(roman_string)):
        if i > 0 and romans[roman_string[i]] > romans[roman_string[i - 1]]:
            result += romans[roman_string[i]] - romans[roman_string[i - 1]] * 2
        else:
            result += romans[roman_string[i]]
    return result
