#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0

    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

    roman_int = 0

    roman_str_len = len(roman_string)

    skip = False
    for i in range(0, roman_str_len):
        if skip:
            skip = False
        else:
            j = i + 1
            cur_num = roman_dict[roman_string[i]]
            if j >= roman_str_len:
                j = None
            if j is not None:
                next_num = roman_dict[roman_string[j]]
                if cur_num < next_num:
                    roman_int += (next_num - cur_num)
                    skip = True
                else:
                    roman_int += cur_num
            else:
                roman_int += cur_num
    return roman_int
