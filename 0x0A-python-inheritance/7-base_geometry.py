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

    def integer_validator(self, name, value):
        """ validate if ``value`` is an integer, raises exception if not """

        if not isinstance(value, int):
            raise TypeError(name, "must be an integer")

        if value <= 0:
            raise ValueError(name, "must be greater than 0")
