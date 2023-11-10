#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    qty = 0
    for t in my_list:
        i, j = t
        total += i * j
        qty += j
    return total/qty
