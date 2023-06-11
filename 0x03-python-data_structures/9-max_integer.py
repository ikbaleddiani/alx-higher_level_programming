#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        v_max = my_list[0]
        for i in my_list:
            if v_max < i:
                v_max = i
        return v_max
