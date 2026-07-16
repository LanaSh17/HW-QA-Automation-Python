import unittest

from homeworks import tree_quantity
from homeworks import count_apostrophes
from homeworks import check_unique_symbols
from homeworks import check_word
from homeworks import reverse_text

class TestHomeworks12(unittest.TestCase):
    def test_tree_quantity(self):
        self.assertEqual(tree_quantity(4), 15)

    def test_tree_quantity_negative(self):
        self.assertNotEqual(tree_quantity(4), 14)

    def test_count_apostrophes(self):
        self.assertEqual(count_apostrophes("Alice's book"), 1)

    def test_count_apostrophes_negative(self):
        self.assertNotEqual(count_apostrophes("Alice book"), 1)

    def test_check_unique_symbols(self):
        self.assertTrue(check_unique_symbols("abcdefghijkl"))

    def test_check_unique_symbols_negative(self):
        self.assertFalse(check_unique_symbols("hello"))

    def test_check_word(self):
        self.assertTrue(check_word("horizon"))

    def test_check_word_negative(self):
        self.assertFalse(check_word("apple"))

    def test_reverse_text(self):
        self.assertEqual(reverse_text("hello"), "olleh")

    def test_reverse_text_negative(self):
        self.assertNotEqual(reverse_text("hello"), "hello")


    if __name__ == "__main__":
            unittest.main()