from unittest import TestCase

from src.binary_trees import BinaryTree, Node

"""
              1
           /     \
          2       3
        /  \     / \
       4    5   6   7
      /
     8
"""

tree = BinaryTree(Node(1))
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)


class TestStringsAlgorithms(TestCase):

    def test_preorder_traversal(self):

        # Positive
        self.assertEqual(BinaryTree.preorder_traversal(tree.root), [1, 2, 4, 8, 5, 3, 6, 7])

        # Negative
        self.assertRaises(TypeError, tree.preorder_traversal)
        self.assertRaises(TypeError, tree.preorder_traversal, tree.root, tree.root)
        self.assertRaises(AttributeError, tree.preorder_traversal, 'Banana')
