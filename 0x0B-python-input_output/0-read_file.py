#!/usr/bin/python3

""" Defines read_file function """


def read_file(filename=""):
    """
    Read file and prints it to the stdout.

    Args:
        filename: The file to read from.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
