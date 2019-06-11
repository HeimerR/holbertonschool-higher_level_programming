#!/usr/bin/python3
"""
unittest
"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.old_stdout = sys.stdout
        sys.stdout = self.mystdout = StringIO()

    def tearDown(self):
        sys.stdout = self.old_stdout

    def test_excep(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_excep2(self):
        with self.assertRaises(ValueError):
            r5 = Rectangle(10, 2)
            r5.width = - 10

    def test_excep3(self):
        with self.assertRaises(TypeError):
            r6 = Rectangle(10, 2)
            r6.x = {}

    def test_excep4(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        r7 = Rectangle(3, 2)
        self.assertEqual(r7.area(), 6)

    def test_display(self):
        r8 = Rectangle(4, 6)
        r8.display()
        self.assertEqual(self.mystdout.getvalue(),
                         "####\n####\n####\n####\n####\n####\n")

    def test_display2(self):
        r8 = Rectangle(2, 2)
        r8.display()
        self.assertEqual(self.mystdout.getvalue(), "##\n##\n")

    def test_display3(self):
        r8 = Rectangle(1, 1)
        r8.display()
        self.assertEqual(self.mystdout.getvalue(), "#\n")

    def test_display4(self):
        r8 = Rectangle(1, 10)
        r8.display()
        self.assertEqual(self.mystdout.getvalue(),
                         "#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n")

    def test_display5(self):
        r8 = Rectangle(2, 3, 2, 2)
        r8.display()
        self.assertEqual(self.mystdout.getvalue(),
                         "\n\n  ##\n  ##\n  ##\n")

    def test_display6(self):
        r8 = Rectangle(3, 2, 1)
        r8.display()
        self.assertEqual(self.mystdout.getvalue(),
                         " ###\n ###\n")

    def test_str(self):
        r8 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r8), "[Rectangle] (12) 2/1 - 4/6")

    def test_str2(self):
        r9 = Rectangle(5, 5, 1)
        self.assertEqual(str(r9), "[Rectangle] ({:d}) 1/0 - 5/5".format(r9.id))

    def test_str3(self):
        r9 = Rectangle(5, 5, 1)
        self.assertEqual(str(r9), "[Rectangle] ({:d}) 1/0 - 5/5".format(r9.id))

    def test_update(self):
        r10 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r10), "[Rectangle] ({:d}) 10/10 - 10/10"
                         .format(r10.id))

    def test_update2(self):
        r11 = Rectangle(10, 10, 10, 10)
        r11.update(89)
        self.assertEqual(str(r11), "[Rectangle] (89) 10/10 - 10/10")

    def test_update3(self):
        r12 = Rectangle(10, 10, 10, 10, 89)
        r12.update(89, 2)
        self.assertEqual(str(r12), "[Rectangle] (89) 10/10 - 2/10")

    def test_update4(self):
        r13 = Rectangle(10, 10, 10, 10)
        r13.update(89, 2, 3)
        self.assertEqual(str(r13), "[Rectangle] (89) 10/10 - 2/3")

    def test_update5(self):
        r14 = Rectangle(10, 10, 10, 10)
        r14.update(89, 2, 3, 4)
        self.assertEqual(str(r14), "[Rectangle] (89) 4/10 - 2/3")

    def test_update6(self):
        r15 = Rectangle(10, 10, 10, 10)
        r15.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r15), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args(self):
        r16 = Rectangle(10, 10, 10, 10)
        r16.update(height=1)
        self.assertEqual(str(r16), "[Rectangle] ({:d}) 10/10 - 10/1"
                         .format(r16.id))

    def test_update_args2(self):
        r17 = Rectangle(10, 10, 10, 10)
        r17.update(width=1, x=2)
        self.assertEqual(str(r17), "[Rectangle] ({:d}) 2/10 - 1/10"
                         .format(r17.id))

    def test_update_args3(self):
        r18 = Rectangle(10, 10, 10, 10)
        r18.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r18), "[Rectangle] (89) 3/1 - 2/10")

    def test_update_args4(self):
        r17 = Rectangle(10, 10, 10, 10)
        r17.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r17), "[Rectangle] ({:d}) 1/3 - 4/2"
                         .format(r17.id))

    def test_to_dict(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(type(r1_dictionary), dict)

    def test_to_dict2(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary,
                         {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

    def test_to_dict3(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertFalse(r1 == r2)

if __name__ == '__main__':
    unittest.main()
