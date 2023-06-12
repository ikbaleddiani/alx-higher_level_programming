#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_list = []
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    for i in range(2):
        list_a.append(0)
        list_b.append(0)
        my_list.append(list_a[i] + list_b[i])
    my_tuple = my_list[0], my_list[1]
    return my_tuple
