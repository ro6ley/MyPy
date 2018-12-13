class MyArray:
    # Initialize the array we will be manipulating
    def __init__(self):
        self.array = []
    
    # Insert an item in the array at a specific index
    def insert(self, item, index):
        self.array.insert(index, item)

    # Traverse the array and print all the items
    def traverse(self):
        for element in self.array:
            print(element)

    # Search for an item in a list and return its index.
    # Return -1 if item cannot be found in the list
    def search(self, item):
        return self.array.index(item) if item in self.array else -1

    # Delete an element from the list
    def delete(self, item):
        element = self.array.index(item)
        del element

    # Updates an element in the list
    def update(self, index, item):
        self.array[index] = item

    # Returns the length of the array
    def length(self):
        return len(self.array)
