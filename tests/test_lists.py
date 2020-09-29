from unittest import TestCase

from src.lists import flatten_list

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

        # Negative
        self.assertRaises(TypeError, flatten_list, 'a')
        self.assertRaises(TypeError, flatten_list, (1, 2))
