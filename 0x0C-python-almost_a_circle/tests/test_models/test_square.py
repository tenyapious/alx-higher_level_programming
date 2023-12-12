#!/usr/bin/python3

""" Define a test class for Rectangle """
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO


class TestSquare(unittest.TestCase):
    """ Test class for Square """

    def test_task10(self):
        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (8) 0/0 - 5')
