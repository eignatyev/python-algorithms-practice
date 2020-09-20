from unittest import TestCase

from src.search import do_binary_search

class TestSearchAlgorithms(TestCase):

    def test_do_binary_search(self):

        # Positive
        self.assertEqual(do_binary_search([-5, 0, 4, 5, 6], -5), 0)
        self.assertEqual(do_binary_search([-5, 0, 4, 5, 6], 4), 2)
        self.assertEqual(do_binary_search([-5, 0, 4, 5, 6], 6), 4)
        self.assertEqual(do_binary_search([-5, 0, 4, 5, 6, 1000], 1000), 5)
        self.assertEqual(do_binary_search([-5, 0, 4, 5, 6, 1000], -5), 0)
        self.assertEqual(do_binary_search(list(range(10000)), 8953), 8953)
        self.assertEqual(do_binary_search('abcdef', 'c'), 2)
        self.assertEqual(do_binary_search('abcdef', 'x'), False)

        # Negative
        self.assertEqual(do_binary_search([], 1), False)
        self.assertEqual(do_binary_search([1, 2, 3], -1), False)
        self.assertEqual(do_binary_search([1, 2, 3], 4), False)
        self.assertRaises(TypeError, do_binary_search)
        self.assertRaises(TypeError, do_binary_search, [1])
        self.assertRaises(TypeError, do_binary_search, 1, 1, 1)
        self.assertRaises(TypeError, do_binary_search, [1, 2, 3], 1, 1, 5)
