class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

    def insert(self, data):
        """
        Compare the new value with the root in order to decide whether to
        insert in the left or right
        """

        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.value:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.value = data

    def print_tree(self):
        # recursively print the left child tree or leaf
        if self.left:
            self.left.print_tree()

        # print the parent
        print(self.value)

        # recursively print the right child tree or leaf
        if self.right:
            self.right.print_tree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(5)

root.print_tree()  # 3, 5, 6, 12, 14
