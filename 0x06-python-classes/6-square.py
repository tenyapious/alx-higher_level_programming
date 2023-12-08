#!/usr/bin/python3

""" Defines a class Square """


class Square:
    """ The Class square """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ Args:
                value (int): size of square
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
        """ Returs:
                Area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """ Prints # number of the square size """
        if self.size > 0:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print("")
        else:
            print("")
