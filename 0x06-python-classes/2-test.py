#!/usr/bin/python3

class P:
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x + 10

    @x.setter
    def x(self, x):
        if x > 20:
            print("it's too big")
            self.__x = 20 
        else:
            self.__x = x

p1 = P(21)

print(p1.x)
