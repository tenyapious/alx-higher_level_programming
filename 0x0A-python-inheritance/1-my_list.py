#!/usr/bin/python3

""" Define a class with a public class that sorts a list """

class MyList(list):
    """ Sort class that inherits from list """

    def print_sorted(self):
        """ Sort and print out instance list """

        print(sorted(self))
