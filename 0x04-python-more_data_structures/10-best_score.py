#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) is not 0:
        valist = list(sorted(a_dictionary.values()))
        num = valist[0]
        for k, v in sorted(a_dictionary.items()):
            if v >= num:
                num = v
                max_score = k
        return max_score
    else:
        return None
