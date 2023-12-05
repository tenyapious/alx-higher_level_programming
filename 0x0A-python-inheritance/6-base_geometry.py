#!/usr/bin/python3

""" Defines ``BaseGeometry`` class """


class BaseGeometry:
    """ An empty BaseGeometry class """

    def area(self):
        """ Calculate the area

        Raises:
            Exception: if area is not implemented
        """

        raise Exception("area() is not implemented")
