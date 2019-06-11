#!/usr/bin/python3
"""
doctest unittest
"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(-1)
        self.b4 = Base(12)
        self.b5 = Base("hola")
        self.b6 = Base(3.1)
        self.b7 = Base()

    def test_setid(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, -1)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, "hola")
        self.assertEqual(self.b6.id, 3.1)
        self.assertEqual(self.b7.id, 3)

    def tearDown(self):
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5
        del self.b6
        del self.b7

if __name__ == '__main__':
    unittest.main()
