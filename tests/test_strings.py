from unittest import TestCase

from src.strings import get_first_letters_as_string


class TestStringsAlgorithms(TestCase):

    def test_get_first_letters_as_string(self):

        # Positive
        self.assertEqual(get_first_letters_as_string('my name is billy'), 'mnib')
        self.assertEqual(get_first_letters_as_string('my Name is billy'), 'mNib')
        self.assertEqual(get_first_letters_as_string(''), '')

        # Negative
        self.assertRaises(TypeError, get_first_letters_as_string)
        self.assertRaises(TypeError, get_first_letters_as_string, 1, [])
        self.assertRaises(AttributeError, get_first_letters_as_string, 1)
