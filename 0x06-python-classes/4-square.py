#!/usr/bin/python3

""" Defines a class Square """


class Square:
    """ Args:
            size (int): size of the square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ Args:
                value (int): size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ Returns:
                Area of the square
        """
        return self.size * self.size
