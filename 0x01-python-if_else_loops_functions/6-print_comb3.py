#!/usr/bin/python3
for i in range(1, 100):
    if i < 10:
        print('{:02d}, '.format(i), end='')
    elif int(str(i)[1:2] + str(i)[:1]) > i:
        for j in range(i + 1, 100):
            if int(str(j)[1:2] + str(j)[:1]) > j:
                print('{}, '.format(i), end='')
                break
        else:
            print('{}'.format(i))
