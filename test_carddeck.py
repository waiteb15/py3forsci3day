#!/usr/bin/env python

import unittest
from card_deck import CardDeck



class TestCardDeck(unittest.TestCase):

    def setUp(self):
        self.d = CardDeck("Test USER")


    def test_deck_len_is_52(self):
        self.assertEqual(52, len(self.d), "Length is not 52")

    def test_drawing_one_card_reduces_length_by_on(self):
        old_len = len(self.d)
        self.d.draw()
        new_len = len(self.d)
        self.assertEqual(1, old_len - new_len, "draw doesnt remove 1 card")
    #
    @unittest.skip
    def test_empty_deck_raises_exception(self):
        with self.assertRaises(ValueError):
            for i in range(53):
                self.d.draw()


if __name__ == '__main__':
    unittest.main(verbosity=11)