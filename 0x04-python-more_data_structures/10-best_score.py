#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        best = list(reversed(sorted(a_dictionary.values())))
        for i in a_dictionary:
            if a_dictionary[i] == best[0]:
                return (i)
    else:
        return None
#        for i, j in a_dictionary.items():
#            if j == best[0]:
#                return i
