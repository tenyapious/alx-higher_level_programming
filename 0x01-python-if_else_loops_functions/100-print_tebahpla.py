#!/usr/local/bin/python3.11
for i in range(90, 64, -1):
    print('{}'.format(chr(i + 32) if i % 2 == 0 else chr(i)), end='')
