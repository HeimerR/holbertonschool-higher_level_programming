#!/usr/bin/python3
""" singly linked list"""


class Node:
    """ class node """
    def __init__(self, data, next_node=None):
        """ init node
        Args:
            data (int):data to store.
            next_node : address next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            locker = Node(self.__head.data, self.__head.next_node)
            prev = None
            while self.__head.next_node is not None:
                if self.__head.data >= value:
                    break
                prev = self.__head
                self.__head = self.__head.next_node
            if self.__head.data <= value:
                new_node.next_node = self.__head.next_node
                self.__head.next_node = new_node
                if locker.next_node is not None:
                        self.__head = locker
            else:
                if prev is None:
                    new_node.next_node = self.__head
                    self.__head = new_node
                else:
                    new_node.next_node = self.__head
                    prev.next_node = new_node
                    if locker.next_node is not None:
                        self.__head = locker
                    if locker.next_node == new_node.next_node:
                        self.__head = prev

    def __str__(self):
        str_list = []
        while self.__head is not None:
            str_list.append(str(self.__head.data))
            str_list.append('\n')
            self.__head = self.__head.next_node
        return ''.join(str_list)
