#!/usr/bin/python3

""" Defines a function `say_my_name` """


def say_my_name(first_name, last_name=""):
    """ Concatenates two strings and print the result

    Args:
        first_name (str): The first string
        last_name (str): The second string

    Raises:
        TypeError: If `first_name` is not a string
            If `second_name` is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if len(last_name) == 0:
        print(first_name)
    else:
        print(first_name, last_name)
