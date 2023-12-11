#!/usr/bin/python3

""" Define a test class TestBase """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ Test Class """

    def test_base(self):
        """ Test method for Base """
        b1 = Base()
        self.assertEqual(b1.id, 1)
