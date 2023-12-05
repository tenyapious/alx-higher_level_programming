#!/usr/bin/python3

""" Defines write_file function """


def write_file(filename="", text=""):
    """
    Write text to file and returns the number characters written.

    Args:
        filename: The file to write to.
        text: The text to write to ``filename``

    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)

    return len(text)
