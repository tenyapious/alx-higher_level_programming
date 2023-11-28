#!/usr/bin/python3

""" Unittest for max_integer([..]) """
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test class for max_integer """

    def test_maxInteger(self):
        """ This test for assertEqual """

        self.assertEqual(max_integer([1, -2, 3.9, 3.4]), 3.9)
        self.assertEqual(max_integer([]), None)
