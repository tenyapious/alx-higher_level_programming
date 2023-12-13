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

    def test_task11(self):
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(str(s1), '[Square] (9) 0/0 - 10')

    def test_task12(self):
        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (10) 0/0 - 5')

        s1.update(20)
        self.assertEqual(str(s1), '[Square] (20) 0/0 - 5')

        s1.update(1, 2)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 2')

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), '[Square] (1) 3/0 - 2')

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), '[Square] (1) 3/4 - 2')

        s1.update(x=12)
        self.assertEqual(str(s1), '[Square] (1) 12/4 - 2')
