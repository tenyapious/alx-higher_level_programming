#!/usr/bin/python3

""" Define a test class for Rectangle """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test class for Rectangle """

    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 2)

        r2 = Rectangle(2, 2)
        self.assertEqual(r2.width, 2)

        r3. Rectangle(2, 2)
        self.assertEqual(r2.area, 4)
