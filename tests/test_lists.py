from unittest import TestCase

from src.lists import flatten_list, FindPairAlgorithms

from random import shuffle

class TestListsAlgorithms(TestCase):

    def test_flatten_list(self):

        # Positive
        self.assertEqual(flatten_list([]), [])
        self.assertEqual(flatten_list([1]), [1])
        self.assertEqual(flatten_list([1, 'a', (1, 2)]), [1, 'a', (1, 2)])
        self.assertEqual(flatten_list([1, 'a', [1, 2]]), [1, 'a', 1, 2])
        self.assertEqual(flatten_list(
            [1, 2, [3, [4, 5, 6], [7, 8, 9]], 10]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )

    def test_find_pair(self):

        list_positives_ordered = list(range(100))
        list_ordered = list(range(-100, 100))
        list_shuffled = [
            -50, 4, 8, -48, -8, -11, 49, -22, 20, -15, 34, 45, -1, 9, 17, 27, 6, -13, 31, -26,
            -47, -4, -7, 35, 19, 12, -5, -32, -36, 30, -33, 26, -45, -37, 29, 36, -40, -9, 16, 47,
            0, -12, 5, 24, 43, 7, -42, 48, 38, -38, -44, 40, -39, -16, -35, 42, 1, -34, 33, -31,
            21, -24, -30, 11, 44, 13, 18, -20, -18, -25, -23, -19, -43, 32, 10, -14, 28, 37, 23, 22,
            15, -46, 46, -21, -3, -17, 39, 25, 2, -49, 41, -27, 14, -10, -2, 3, -6, -29, -41, -28
        ]

        # Positive
        self.assertEqual(FindPairAlgorithms.iteration(list_positives_ordered, 99), (0, 99))
        self.assertEqual(FindPairAlgorithms.two_pointer(list_positives_ordered, 99), (0, 99))
        self.assertEqual(FindPairAlgorithms.iteration(list_ordered, 0), (-99, 99))
        self.assertEqual(FindPairAlgorithms.two_pointer(list_ordered, 0), (-99, 99))
        self.assertEqual(FindPairAlgorithms.iteration(list_shuffled, 37), (4, 33))
        self.assertEqual(FindPairAlgorithms.two_pointer(list_shuffled, 37), (-12, 49))

        # Negative
        self.assertEqual(FindPairAlgorithms.iteration([], 99), False)
        self.assertEqual(FindPairAlgorithms.two_pointer([], 99), False)
        self.assertEqual(FindPairAlgorithms.iteration(list_positives_ordered, 0), False)
        self.assertEqual(FindPairAlgorithms.two_pointer(list_positives_ordered, 0), False)
        self.assertEqual(FindPairAlgorithms.iteration(list_ordered, 198), False)
        self.assertEqual(FindPairAlgorithms.two_pointer(list_ordered, 198), False)
