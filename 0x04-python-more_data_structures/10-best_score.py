#!/usr/bin/python3

def best_score(a_dictionary):
    best = list(reversed(sorted(a_dictionary.values())))
    if len(a_dictionary) == 0:
        return None
    else:
        for i, j in a_dictionary.items():
            if j == best[0]:
                return i
            continue
        return i
