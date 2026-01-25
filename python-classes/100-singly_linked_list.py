#!/usr/bin/python3
"""Defines a singly linked list with sorted insertion."""


class Node:
    """Represents a node in a singly linked list.

    Attributes:
        __data (int): Private attribute storing node data.
        __next_node (Node or None): Private attribute storing next node reference.
    """

    def __init__(self, data, next_node=None):
        """Initializes a new Node instance.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the list. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data stored in the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node in the list.

        Returns:
            Node or None: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the list.

        Args:
            value (Node or None): The new next node.

        Raises:
            TypeError: If value is not a Node object and not None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list.

    Attributes:
        __head (Node or None): Private attribute storing the head of the list.
    """

    def __init__(self):
        """Initializes a new empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node with the given value in sorted (increasing) order.

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)

        # If list is empty or new value should be at the beginning
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Find the appropriate position to insert
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        # Insert the new node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the entire list.

        Returns:
            str: Each node's data on a separate line.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
