#!/usr/bin/python3

class P:
    def __init__(self, x):
        self.x = x

    @property
    def xx(self):
        return self.__x

    @xx.setter
    def xx(self, x):
        if x > 20:
            print("it's too big")
            self.__x = x
        else:
            self.__x = x

p1 = P(21)

print(p1.x)
