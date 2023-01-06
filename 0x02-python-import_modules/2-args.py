#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argumentStr = "{:d} argument"
    argc = len(sys.argv) - 1

    if argc == 0:
        argumentStr += 'S.'
    elif argc == 1:
        argumentStr += ':'
    else:
        argumentStr += 'S:'
    print(argumentStr.format(argc))

    i = 0
    for argument in sys.argv:
        if i != 0:
            print("{:d}: {:s}".format(i, argument))
        i += 1
