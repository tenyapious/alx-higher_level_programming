#!/usr/bin/python3

""" Define a test class for Rectangle """
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):
    """ Test class for Rectangle """

    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 2)

        r2 = Rectangle(2, 2)
        self.assertEqual(r2.width, 2)

        r3 = Rectangle(3, 2)
        self.assertEqual(r3.area(), 6)

        displayed_output = StringIO()
        with patch('sys.stdout', new = displayed_output):
            r4 = Rectangle(1, 1)
            r4.display()

            printed_str = displayed_output.getvalue().strip()
            self.assertEqual(printed_str, '#')

            r6 = Rectangle(1, 1, 2, 2)
            r6.display()

            printed_str = displayed_output.getvalue().strip()
            self.assertEqual(printed_str, '#\n\n\n  #')

        r5 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r5), '[Rectangle] (12) 2/1 - 4/6')
