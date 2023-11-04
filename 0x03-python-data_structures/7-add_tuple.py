#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta_len = len(tuple_a)
    tb_len = len(tuple_b)
    
    if ta_len < 2:
        a_2 = 0
    else:
        a_2 = tuple_a[1]

    if ta_len < 1:
        a_1 = 0
    else:
        a_1 = tuple_a[0]

    if tb_len < 2:
        b_2 = 0
    else:
        b_2 = tuple_b[1]

    if tb_len < 1:
        b_1 = 0
    else:
        b_1 = tuple_b[0]

    return (a_1 + b_1, a_2 + b_2)
