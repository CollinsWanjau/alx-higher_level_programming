#!/usr/bin/python3
"""module for a singly linked list"""


class Node:
    """defines a node"""

    def __init__(self, data, next_node=None):
        """
        Initialized class node with data
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node
        """
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """Simple instantiation
        """
        self.head = None

    def __str__(self):
        """Should be printable
        """
        printssl = ""
        current = self.head
        while current:
            printssl += str(current.data) + "\n"
            current = current.next_node
        return printssl[:-1]

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position
        in the list
        """
        new = Node(value)
        # special case for the empty list
        if self.head is None:
            self.head = new
            return
        # special case for head at the end
        elif self.head.data >= value:
            new.next_node = self.head
            self.head = new
            return
        else:
            # Locate the node before the point of intersection
            current = self.head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node
            if current.next_node:
                new.next_node = current.next_node
            current.next_node = new
