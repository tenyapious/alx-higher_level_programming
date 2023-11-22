#!/usr/bin/python3

""" Define a class Square """


class Square:
    """ A class Sqaure """

    def __init__(self, size=0):
        """ Args:
                size (int): size of the square
        """
        self.__size = size

    def area(self):
        return self.__size * self.__size
