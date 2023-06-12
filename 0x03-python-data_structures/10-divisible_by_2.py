#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul_by2 = []
    for i in my_list:
        if i % 2 == 0:
            mul_by2.append(True)
        else:
            mul_by2.append(False)
    return mul_by2
