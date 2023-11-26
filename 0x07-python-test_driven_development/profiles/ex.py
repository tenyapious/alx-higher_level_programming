#!/usr/bin/python3

""" Defines a function that adds 2 integers or float and returns the result
"""


@profile
def add_integer(a, b=98):
    """ Adds two integers or floats together

    Args:
        a: The first integer or float
        b: The second integer or float. Defaults to 98.

    Returns:
        The result of adding a and b

    Raises:
        TypeError: If a is neither an integer nor float.
            If b is neither an integer nor float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
add_integer(2,3)
