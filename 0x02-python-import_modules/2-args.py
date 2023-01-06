#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) - 1 = 1:
        print("{:d} argument:".format(len(sys.argv) - 1))
    elif len(sys.argv) - 1 > 1:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    else:
        print("0 arguments.")

count = 0
    while count < (len(sys.argv) - 1):
        print("{:d}: {:s}".format(count + 1, sys.argv[count]))
