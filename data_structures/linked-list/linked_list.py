"""
This is an implementation of a linked list in Python.

A linked list consists of nodes and each node contains a value and a pointer to
another node. The starting node is known as a Header.

Advantages:
- It saves memory by only allocating the memory required for values to be 
  stored. With arrays you have to set an array size before filling it.
- Nodes can live anywhere in memory whereas an array requires a sequence of
  memory to be initiated.

Disadvantages:
- Linear look up time since when looking for a value in a linked list, you 
  have to start from the beginning and check an element at a time.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None  # it initially points to nothing

    def traverse(self):
        node = self
        while node is not None:
            print(node.val)  # print the value
            node = node.next  # move to the next node

# create a linked list the following way
node1 = Node(10)
node2 = Node(23)
node3 = Node(35)

node1.next = node2
node2.next = node3

# the linked list now looks like: 10->23->35
node1.traverse()

"""
Test cases:
- Create a linked list
- Traverse a linked list
"""
