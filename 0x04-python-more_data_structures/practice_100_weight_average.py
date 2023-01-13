#!/usr/bin/python3

average_weight = __import__("100-weight_average").weight_average

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]

result = average_weight(my_list)
print("Average: {:0.2f}".format(result))
