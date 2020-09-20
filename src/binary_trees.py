class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():

    def __init__(self, root):
        self.root = root

    @staticmethod
    def preorder_traversal(start):
        traversal = []
        if start:
            traversal.append(start.value)
            traversal.extend(BinaryTree.preorder_traversal(start.left))
            traversal.extend(BinaryTree.preorder_traversal(start.right))
        return traversal
