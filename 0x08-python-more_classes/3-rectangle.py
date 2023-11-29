#!/usr/bin/python3

""" Module to define a class Rectangle that defines a rectangle """


class Rectangle:
    """ The class Rectangle """

    def __init__(self, width=0, height=0):
        """ Args:
                width: width of the rectangle.
                height: height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns: The width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Args:
                value (int): The new width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns: The height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Args:
                value (int): The new height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns: The area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns: 0 if width or height is 0
                or the parameter of the rectangle
        """
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ Returns: The string representation
            of the rectangle with the character #
        """
        s = ""
        for i in range(self.__height):
            for j in range(self.width):
                s += "#"
            if i != self.__height - 1:
                s += "\n"
        return s
