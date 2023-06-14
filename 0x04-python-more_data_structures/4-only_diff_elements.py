#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    clean_set = []
    for elements in set_1 ^ set_2:
        clean_set.append(elements)
    return clean_set
