#!/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        best_score_val = 0
        for key in list(a_dictionary):
            if a_dictionary[key] > best_score_val:
                best_score_val = a_dictionary[key]
        return best_score_val
    return None
