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
        """ validate if ``value`` is an integer, raises exception if not

        Raises:
            TypeError: if ``value`` is not an integer.
            ValueError: if ``value`` is less or equal to zero.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
