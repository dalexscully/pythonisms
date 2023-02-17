class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, collection=None):
        # Initialize a new LinkedList object with an optional collection of items
        # The head of the list is set to None by default
        # If a collection is provided, insert each item into the list in reverse order
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def __str__(self):
        # Return a string representation of the LinkedList object
        # Traverse the list and build a string containing the value of each node
        # separated by " -> " and ending with "None"
        out = ""
        for value in self:
            out += f"[ {value} ] -> "
        return out + "None"

    def insert(self, value):
        # Insert a new node with the specified value at the beginning of the list
        # The new node becomes the head of the list, and the previous head becomes
        # the next node in the list
        self.head = Node(value, self.head)

    def __iter__(self):
        # Define an iterator for the LinkedList object
        # The iterator generates a sequence of values by traversing the list
        # starting from the head node
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()

    def __len__(self):
        # Return the length of the LinkedList object
        # This is implemented using the built-in `len` function, which converts
        # the LinkedList object to a list and returns the length of the list
        return len(list(iter(self)))

    def __eq__(self, other):
        # Determine whether two LinkedList objects are equal
        # This is done by comparing the two objects as lists, i.e., by converting
        # both LinkedList objects to lists and checking whether they have the same values
        return list(self) == list(other)

    def __getitem__(self, index):
        # Get the value of the node at the specified index in the list
        # If the index is negative, raise an IndexError
        # If the index is out of bounds, raise an IndexError
        # Otherwise, traverse the list and return the value of the node
        # at the specified index
        if index < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError

