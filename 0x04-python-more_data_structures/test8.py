#!/usr/bin/python3

tel = {'jack': 4098, 'sape': 4139}
key = 'jack'

if key in tel:
    del tel[key]

print(tel)
