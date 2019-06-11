#!/usr/bin/python3
""" module rectangle"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width"""
        return self.__width

    @property
    def height(self):
        """height"""
        return self.__height

    @property
    def x(self):
        """x"""
        return self.__x

    @property
    def y(self):
        """y"""
        return self.__y

    @width.setter
    def width(self, value):
        """width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area"""
        return self.__width * self.__height

    def display(self):
        """display"""
        print('\n' * self.__y + (" " * self.__x +
              (('#' * self.__width) + '\n')) * self.__height, end='')

    def __str__(self):
        """str"""
        str1 = ("[{}] ({:d}) {:d}/{:d} - {:d}".format
                (type(self).__name__, self.id, self.__x,
                 self.__y, self.__width))
        if type(self).__name__ == 'Rectangle':
            str1 = str1 + "/{:d}".format(self.__height)
        return str1

    def update(self, *args, **kwargs):
        """update"""
        attrs = [self.id, self.__width, self.__height, self.__x, self.__y]
        var = ('id', 'width', 'height', 'x', 'y')
        if kwargs is not None and (args is None or len(args) is 0):
            for key, value in kwargs.items():
                if key in var:
                    attrs[var.index(key)] = value
            (self.id, self.__width, self.__height, self.__x, self.__y) = attrs
        else:
            args_aux = list(attrs[i] for i in range(len(args), 5))
            args_aux2 = list(args) + args_aux
            (self.id, self.__width, self.__height,
             self.__x, self.__y) = args_aux2

    def to_dictionary(self):
        """to dictionary"""
        new_dict = {'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y}
        return new_dict
