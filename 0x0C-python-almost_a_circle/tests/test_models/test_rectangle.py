#!/usr/bin/python3

""" Define a test class for Rectangle """
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square
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

        r5.update(89)
        self.assertEqual(str(r5), '[Rectangle] (89) 2/1 - 4/6')

        r5.update(89, 2)
        self.assertEqual(str(r5), '[Rectangle] (89) 2/1 - 2/6')

        r5.update(89, 2, 3)
        self.assertEqual(str(r5), '[Rectangle] (89) 2/1 - 2/3')

        r5.update(89, 2, 3, 4)
        self.assertEqual(str(r5), '[Rectangle] (89) 4/1 - 2/3')

        r5.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r5), '[Rectangle] (89) 4/5 - 2/3')

    def test_task9(self):
        """ Run test for task 9 """

        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')

        r1.update(height=1)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/1')

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 1/1')

        r1.update(y=1, width=2, x=3, id=8)
        self.assertEqual(str(r1), '[Rectangle] (8) 3/1 - 2/1')

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), '[Rectangle] (8) 1/3 - 4/2')

    def test_task10(self):
        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (7) 0/0 - 5')
