#!/usr/bin/python3

""" Defines a function ``text_identation`` """


def text_indentation(text):
    """ Prints a text with 2 new lines after \
            each of these characters: ".","?" and ":"

    Args:
        text (str): The text to print new lines after the characters

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = True
    start = 0

    for idx, x in enumerate(text):
        if new_line:
            if x == " ":
                continue
            start = idx
            new_line = False

        if x == "." or x == "?" or x == ":":
            print(text[start:idx+1])
            print()
            new_line = True

    if not new_line:
        while (text[idx] == " "):
            idx -= 1
        print(text[start:idx+1], end="")
