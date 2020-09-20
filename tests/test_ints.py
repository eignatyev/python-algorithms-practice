from unittest import TestCase

from src.ints import get_odds_by_N


class TestIntsAlgorithms(TestCase):

    def test_get_odds_by_N(self):

        # Positive
        self.assertEqual(get_odds_by_N(5, 13), 39)
        self.assertEqual(get_odds_by_N(0, 50), 0)
        self.assertEqual(get_odds_by_N(1, 5), 5)
        self.assertEqual(get_odds_by_N(2, 5), 5)
        self.assertEqual(get_odds_by_N(2, 0), 0)

        # Negative
        self.assertRaises(TypeError, get_odds_by_N)
        self.assertRaises(TypeError, get_odds_by_N, 1, 2, 3)
        self.assertRaises(TypeError, get_odds_by_N, 1, None)
