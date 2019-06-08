#!/usr/bin/python3
"""
module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        Rectangle.width.fset(self, value)
        Rectangle.height.fset(self, value)

    def update(self, *args, **kwargs):
        if kwargs != None and (args == None or len(args) == 0):
            if 'size' in kwargs.keys():
                print("hola")
                aux = {'width': kwargs['size'], 'height': kwargs['size']}
                kwargs.update(aux)
        args_list = list(args)
        if len(args) > 1:
            args_list.insert(1, args[1])
        super().update(*args_list)
            
