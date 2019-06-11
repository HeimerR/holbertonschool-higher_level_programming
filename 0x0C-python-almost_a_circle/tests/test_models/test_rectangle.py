#!/usr/bin/python3
"""
unittest
"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
"""import sys
from contextlib import contextmanager
from StringIO import StringIO
"""

"""
@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err
"""


class TestRectangle(unittest.TestCase):

    """def test_setrectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 3)
    def test_setrectangle2(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 4)
    def test_setrectangle3(self):
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.id, 5)
    def test_setrectangle4(self):
        r4 = Rectangle(10, 2, 0, 0,12)
        self.assertEqual(r4.id, 12)

    """

    def test_excep(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
  
    def test_excep2(self):
        with self.assertRaises(ValueError):
            r5 = Rectangle(10, 2)
            r5.width= -10

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

    """def test_display(self):
        with captured_output() as (out, err):
            r8 = Rectangle(4, 6)
            r8.display()
            lines = out.getvalue().strip()
            self.assertEqual("####\n####\n####\n####\n####\n####\n", lines)
    """
    def test_str(self):
        r8 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r8), "[Rectangle] (12) 2/1 - 4/6")

    def test_str2(self):
        r9 = Rectangle(5, 5, 1)
        self.assertEqual(str(r9), "[Rectangle] ({:d}) 1/0 - 5/5".format(r9.id))

    def test_str2(self):
        r9 = Rectangle(5, 5, 1)
        self.assertEqual(str(r9), "[Rectangle] ({:d}) 1/0 - 5/5".format(r9.id))

    def test_update(self):
        r10 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r10), "[Rectangle] ({:d}) 10/10 - 10/10".format(r10.id))

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
        self.assertEqual(str(r16), "[Rectangle] ({:d}) 10/10 - 10/1".format(r16.id))

    def test_update_args2(self):
        r17 = Rectangle(10, 10, 10, 10)
        r17.update(width=1, x=2)
        self.assertEqual(str(r17), "[Rectangle] ({:d}) 2/10 - 1/10".format(r17.id))

    def test_update_args3(self):
        r18 = Rectangle(10, 10, 10, 10)
        r18.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r18), "[Rectangle] (89) 3/1 - 2/10")

    def test_update_args4(self):
        r17 = Rectangle(10, 10, 10, 10)
        r17.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r17), "[Rectangle] ({:d}) 1/3 - 4/2".format(r17.id))

if __name__ == '__main__':
    unittest.main()
