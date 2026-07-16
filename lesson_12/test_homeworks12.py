import unittest

from homeworks import tree_quantity
from homeworks import count_apostrophes
from homeworks import check_unique_symbols
from homeworks import check_word
from homeworks import reverse_text

# 1. tree_quantity
    def test_tree_quantity_positive(self):
        self.assertEqual(tree_quantity(4), 15)

    def test_tree_quantity_negative_type(self):
        with self.assertRaises(TypeError):
            tree_quantity("String")

    # 2. count_apostrophes
    def test_count_apostrophes_positive(self):
        self.assertEqual(count_apostrophes("Alice's book"), 1)

    def test_count_apostrophes_without_apostrophe(self):
        self.assertEqual(count_apostrophes("Alice book"), 0)

    # 3. check_unique_symbols
    def test_check_unique_symbols_positive(self):
        self.assertTrue(check_unique_symbols("abcdefghijkl"))

    def test_check_unique_symbols_negative(self):
        self.assertFalse(check_unique_symbols("aaaaaa"))

    # 4. check_word
    def test_check_word_positive(self):
        self.assertTrue(check_word("horizon"))

    def test_check_word_negative(self):
        self.assertFalse(check_word("apple"))

    # 5. reverse_text
    def test_reverse_text_positive(self):
        self.assertEqual(reverse_text("hello"), "olleh")

    def test_reverse_text_negative_type(self):
        with self.assertRaises(TypeError):
            reverse_text(13)


    if __name__ == "__main__":
            unittest.main()