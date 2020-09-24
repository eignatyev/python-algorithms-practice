from unittest import TestCase

from src.strings import get_first_letters_as_string, is_brackets_balanced


class TestStringsAlgorithms(TestCase):

    def test_get_first_letters_as_string(self):

        # Positive
        self.assertEqual(get_first_letters_as_string('my name is billy'), 'mnib')
        self.assertEqual(get_first_letters_as_string('my Name is billy'), 'mNib')
        self.assertEqual(get_first_letters_as_string(''), '')

        # Negative
        self.assertRaises(TypeError, get_first_letters_as_string)
        self.assertRaises(TypeError, get_first_letters_as_string, 1, [])
        self.assertRaises(TypeError, get_first_letters_as_string, 1)

    def test_is_brackets_balanced(self):

        # Positive
        self.assertEqual(is_brackets_balanced('()'), True)
        self.assertEqual(is_brackets_balanced('{[()]}'), True)
        self.assertEqual(is_brackets_balanced('11(0{00}011)sss[]{[()]}aaa'), True)
        self.assertEqual(is_brackets_balanced(''), True)
        self.assertEqual(is_brackets_balanced('[                   ()                     ]'), True)

        # Negative
        self.assertEqual(is_brackets_balanced(')('), False)
        self.assertEqual(is_brackets_balanced('()('), False)
        self.assertEqual(is_brackets_balanced('())'), False)
        self.assertEqual(is_brackets_balanced(')()'), False)
        self.assertEqual(is_brackets_balanced('(()'), False)
        self.assertEqual(is_brackets_balanced('11(0{00}011)sss[]{[()]aaa'), False)
        self.assertEqual(is_brackets_balanced('11(0{00}011)sss[][()]}aaa'), False)

        self.assertRaises(TypeError, is_brackets_balanced)
        self.assertRaises(TypeError, is_brackets_balanced, 1)
