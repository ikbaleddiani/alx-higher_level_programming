#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = ""
    best_score = 0
    for key in a_dictionary:
        if best_score < a_dictionary[key]:
            best_score = a_dictionary[key]
            best_key = key
    return best_key 
