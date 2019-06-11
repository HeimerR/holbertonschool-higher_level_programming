#!/usr/bin/python3
"""
doctest unittest
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import sys
from io import StringIO
import json


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(-1)
        cls.b4 = Base(12)
        cls.b5 = Base("hola")
        cls.b6 = Base(3.1)
        cls.b7 = Base()

    def test_setid(self):
        self.assertEqual(self.b1.id, 1)
    def test_setid2(self):
        self.assertEqual(self.b2.id, 2)
    def test_setid3(self):
        self.assertEqual(self.b3.id, -1)
    def test_setid4(self):
        self.assertEqual(self.b4.id, 12)
    def test_setid5(self):
        self.assertEqual(self.b5.id, "hola")
    def test_setid6(self):
        self.assertEqual(self.b6.id, 3.1)
    def test_setid7(self):
        self.assertEqual(self.b7.id, 3)

    def setUp(self):
        self.old_stdout = sys.stdout
        sys.stdout = self.mystdout = StringIO()
    
    def tearDown(self):
        sys.stdout = self.old_stdout
        
    @classmethod
    def tearDownClass(cls):
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4
        del cls.b5
        del cls.b6
        del cls.b7

    def test_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_json_string2(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        list_back = json.loads(json_dictionary)
        self.assertEqual(list_back, [dictionary])

if __name__ == '__main__':
    unittest.main()
