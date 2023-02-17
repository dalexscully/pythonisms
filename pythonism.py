class MyCollection:
    def __init__(self, data=None):
        self.data = data
        self.index = 0

    def __str__(self):
        return str(self.data)

    def __iter__(self):
        # Define the iterator by returning a generator that yields each value in the data
        for value in self.data:
            yield value

    def to_list(self):
        # Convert the collection to a list by creating a new list from the iterator
        return list(self)

    def __len__(self):
        # Return the length of the data
        return len(self.data)

    def __getitem__(self, index):
        # Return the value at the specified index in the data list
        return self.data[index]

    def __contains__(self, value):
        # Check if the specified value is in the data
        return value in self.data

    def __reversed__(self):
        # Return a new MyCollection object that contains the data in reverse
        return MyCollection(reversed(self.data))


