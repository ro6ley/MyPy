class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def in_order(root):
    """
    In order traversal starts at the left node, then the root, then the right
    node, recursively
    """
    if root:
        in_order(root.left)
        print(root.value)
        in_order(root.right)


def pre_order(root):
    """
    Pre order traversal starts at the root node, then the left, then the right
    node, recursively
    """
    if root:
        print(root.value)
        pre_order(root.left)
        pre_order(root.right)


def post_order(root):
    """
    Post order traversal starts at the left node, then the right, then the root
    node, recursively
    """
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.value)


# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\nIn order traversal: ")
in_order(root)

print("\nPre order traversal: ")
pre_order(root)

print("\nPost order traversal: ")
post_order(root)
