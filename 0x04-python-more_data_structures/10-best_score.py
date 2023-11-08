#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary):
        best_score_key = ''
        best_score_val = 0
        for key in list(a_dictionary):
            if a_dictionary[key] > best_score_val:
                best_score_key = key
                best_score_val = a_dictionary[key]
        return best_score_key
    return None
