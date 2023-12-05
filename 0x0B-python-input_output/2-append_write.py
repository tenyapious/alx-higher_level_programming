#!/usr/bin/python3

""" Defines append_write function """


def append_write(filename="", text=""):
    """
    Appends text to file and returns the number of characters written.

    Args:
        filename: The file name to append ``text``.
        text: The text to append to ``filename``.

    Returns:
        int: The number of character appended to ``filename``.
    """

    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)

    return len(text)
