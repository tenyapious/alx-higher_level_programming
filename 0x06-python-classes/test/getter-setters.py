#!/usr/bin/python3

class Example:

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = 2+x

ex = Example(4)

x = ex.x

print(x)
