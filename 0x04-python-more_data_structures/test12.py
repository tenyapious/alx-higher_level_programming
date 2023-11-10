#!/usr/bin/python3
rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

rom_str = "MMCDXXI"
rom_int = 0

rom_str_len = len(rom_str)

skip = False
for i in range(0, rom_str_len):
    if skip:
        skip = False
    else:
        j = i + 1
        cur_num = rom_dict[rom_str[i]]
        if j >= rom_str_len:
             j = None
        if j is not None:
            next_num = rom_dict[rom_str[j]]
            if cur_num < next_num:
               rom_int += (next_num - cur_num)
               skip = True
            else:
                rom_int += cur_num
        else:
            rom_int += cur_num
print(rom_int)
