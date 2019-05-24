#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test
    """
    def test_integers(self):
        test_list = [2, 3, 5, 1, 0]
        self.assertEqual(5, max_integer(test_list))

    def test_negative_integers(self):
        test_list = [-2, -3, -5, -1, 0]
        self.assertEqual(0, max_integer(test_list))

    def test_empty_list(self):
        test_list = []
        self.assertEqual(None, max_integer(test_list))

    def test_wrong_type(self):
        test_list = [1, "hola"]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_tupla(self):
        test_list = (1, 2)
        self.assertEqual(2, max_integer(test_list))

    def test_float(self):
        test_list = [1.2, 2.5]
        self.assertEqual(2.5, max_integer(test_list))

if __name__ == '__main__':
    unittest.main()    
