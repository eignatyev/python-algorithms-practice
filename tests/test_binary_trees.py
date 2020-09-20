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


class TestBinaryTreesAlgorithms(TestCase):

    def test_pre_order_traversal(self):

        # Positive
        self.assertEqual(BinaryTree.pre_order_traversal(tree.root), [1, 2, 4, 8, 5, 3, 6, 7])

        # Negative
        self.assertRaises(TypeError, BinaryTree.pre_order_traversal)
        self.assertRaises(TypeError, BinaryTree.pre_order_traversal, tree.root, tree.root)
        self.assertRaises(AttributeError, BinaryTree.pre_order_traversal, 'Banana')

    def test_in_order_traversal(self):

        # Positive
        self.assertEqual(BinaryTree.in_order_traversal(tree.root), [8, 4, 2, 5, 1, 6, 3, 7])

        # Negative
        self.assertRaises(TypeError, BinaryTree.in_order_traversal)
        self.assertRaises(TypeError, BinaryTree.in_order_traversal, tree.root, tree.root)
        self.assertRaises(AttributeError, BinaryTree.in_order_traversal, 'Banana')

    def test_post_order_traversal(self):

        # Positive
        self.assertEqual(BinaryTree.post_order_traversal(tree.root), [8, 4, 5, 2, 6, 7, 3, 1])

        # Negative
        self.assertRaises(TypeError, BinaryTree.post_order_traversal)
        self.assertRaises(TypeError, BinaryTree.post_order_traversal, tree.root, tree.root)
        self.assertRaises(AttributeError, BinaryTree.post_order_traversal, 'Banana')
