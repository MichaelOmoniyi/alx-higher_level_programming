#!/usr/bin/python3
import sys

if __name__ == "__main__":

    result = 0
    i = 0

    for argument in sys.argv:
        if i != 0:
            result += int(argument)
        else:
            i += 1
    print("{:d}.format(result))
