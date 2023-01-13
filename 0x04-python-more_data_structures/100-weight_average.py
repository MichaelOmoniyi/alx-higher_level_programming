#!/usr/bin/python3

def weight_average(my_list=[]):
    total = 0
    average = 0
    if len(my_list) == 0:
        return 0
    for row in my_list:
        total += row[0] * row[1]
        average += row[1]
    return (total/average)
