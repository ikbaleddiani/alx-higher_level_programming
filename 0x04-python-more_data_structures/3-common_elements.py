#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_elem = []
    for element in set_1:
        if element in set_2:
            common_elem.append(element)
    return common_elem
