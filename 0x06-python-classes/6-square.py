#!/usr/bin/python3

""" Defines a class Square """


class Square:
    """ The class Sqaure

        Args:
            size (int): size of the square
            position (tuple): tuple of 2 positive integers
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Args:
                value (int): the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """ Args:
            value (tuple): value of the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ Returns:
                The area of the square """
        return self.size * self.size

    def my_print(self):
        """ Prints # in place of the the size of the square """
        if self.size > 0:
            for i in range(0, self.position[1]):
                print("")
            for i in range(0, self.size):
                for k in range(0, self.position[0]):
                    print(" ", end="")
                for j in range(0, self.size):
                    print("#", end="")
                print("")
        else:
            print("")
