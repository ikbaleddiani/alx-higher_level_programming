#!/usr/bin/python3
def new_in_list(new_list, idx, element):
    if idx in range(len(new_list)):
        new_list[idx] = element
    return new_list
