import unittest
from game.deck import Deck
from game.card import Card

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_shuffle(self):
        original_order = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.cards)

    def test_draw_card(self):
        card = self.deck.draw()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(self.deck.cards), 51)

    def test_draw_card_empty_deck(self):
        self.deck.cards = []  # Empty the deck
        card = self.deck.draw()
        self.assertIsNone(card)

if __name__ == '__main__':
    unittest.main()