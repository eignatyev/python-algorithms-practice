class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():

    def __init__(self, root):
        self.root = root

    @staticmethod
    def pre_order_traversal(start):  # Root -> Left -> Right
        traversal = []
        if start:
            traversal.append(start.value)
            traversal.extend(BinaryTree.pre_order_traversal(start.left))
            traversal.extend(BinaryTree.pre_order_traversal(start.right))
        return traversal

    @staticmethod
    def in_order_traversal(start):  # Left -> Root -> Right
        traversal = []
        if start:
            traversal.extend(BinaryTree.in_order_traversal(start.left))
            traversal.append(start.value)
            traversal.extend(BinaryTree.in_order_traversal(start.right))
        return traversal

    @staticmethod
    def post_order_traversal(start):  # Left -> Right -> Root
        traversal = []
        if start:
            traversal.extend(BinaryTree.post_order_traversal(start.left))
            traversal.extend(BinaryTree.post_order_traversal(start.right))
            traversal.append(start.value)
        return traversal
