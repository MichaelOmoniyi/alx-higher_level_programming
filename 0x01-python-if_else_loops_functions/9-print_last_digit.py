#!/usr/bin/python3
def print_last_digit(number):
    ldigit = abs(number) % 10

    if number < 0:
        ldigit = -(ldigit)
        return ldigit
    else:
        return ldigit
