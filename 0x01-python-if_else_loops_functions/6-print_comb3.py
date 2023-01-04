#!/usr/bin/python3
for count1 in range(0, 10):
    for count2 in range(0, 10):
        if count1 == 9 and count2 == 9:
            print("{:d}{:d}".format(count1, count2))
        elif count1 == 1 and count2 == 0:
            continue
        else:
            print("{:d}{:d}, ".format(count1, count2), end="")
