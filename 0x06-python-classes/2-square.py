#!/usr/bin/python3

""" Define a class Square """


class Square:
    """ A class Sqaure """

    def __init__(self, size=0):
        """ Args:
                size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """ int: the size of the square """
        return self.__size

    @size.setter
    def size(self, size):
        if (type(size) is not int):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
