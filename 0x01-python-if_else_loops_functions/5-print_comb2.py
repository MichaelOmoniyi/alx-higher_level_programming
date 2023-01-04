#!/usr/bin/python3
for count1 in range(0, 10):
    for count2 in range(0, 10):
        if count1 == 9 and count2 == 9:
            print("{:d}{:d}".format(count1, count2))
        else:
            print("{:d}{:d}, ".format(count1, count2), end="")
