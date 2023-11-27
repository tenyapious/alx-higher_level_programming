#!/usr/bin/python3

""" Defines a function `print_square` """


def print_square(size):
    """ Prints a square with the character #

    Args:
        size (int): size length of the square

    Raises:
        TypeError: If `size` is not an integer
            If `size` is a float and less than 0.
        ValueError: If `size` is less than 0
    """

    if isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
        else:
            size = int(size)
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
