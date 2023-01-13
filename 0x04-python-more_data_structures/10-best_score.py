#!/usr/bin/python3

def best_score(a_dictionary):
    best = list(reversed(sorted(a_dictionary.values())))
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        for i in a_dictionary:
            if a_dictionary[i] == best[0]:
                return (i)
#        for i, j in a_dictionary.items():
#            if j == best[0]:
#                return i
