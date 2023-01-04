#!/usr/bin/python3
def print_last_digit(number):
    ldigit = abs(number) % 10

    if number < 0:
        ldigit = -(ldigit)
        print("{ldigit}")
    else:
        print("{ldigit}")
