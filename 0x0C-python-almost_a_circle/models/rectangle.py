#!/usr/bin/python3

""" Defines the class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ The class Rectangle

    Args:
        width: Width of the rectangle.
        height: Height of the rectangle.
        x: X cordinate of the rectangle.
        y: Y cordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """ Return the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """ Return the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        """ Return the x cordinate of the rectangle """
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """ Return the y cordinate of the rectangle """
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
