import unittest
from game.hand import Hand
from game.card import Card

class TestHand(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()

    def test_initial_value(self):
        self.assertEqual(self.hand.value(), 0)

    def test_add_card(self):
        card = Card('10', 'Hearts')
        self.hand.cards.append(card)
        self.assertEqual(self.hand.value(), 10)

    def test_add_face_card(self):
        card = Card('King', 'Spades')
        self.hand.cards.append(card)
        self.assertEqual(self.hand.value(), 10)

    def test_add_ace(self):
        card = Card('Ace', 'Diamonds')
        self.hand.cards.append(card)
        self.assertEqual(self.hand.value(), 11)

    def test_add_multiple_cards(self):
        self.hand.cards.append(Card('10', 'Hearts'))
        self.hand.cards.append(Card('Ace', 'Diamonds'))
        self.assertEqual(self.hand.value(), 21)

    def test_bust_with_aces(self):
        self.hand.cards.append(Card('Ace', 'Diamonds'))
        self.hand.cards.append(Card('Ace', 'Clubs'))
        self.hand.cards.append(Card('10', 'Hearts'))
        self.assertEqual(self.hand.value(), 12)  # Aces count as 1

    def test_bust_without_aces(self):
        self.hand.cards.append(Card('10', 'Hearts'))
        self.hand.cards.append(Card('Queen', 'Diamonds'))
        self.hand.cards.append(Card('King', 'Clubs'))
        self.assertEqual(self.hand.value(), 30)  # Bust

if __name__ == '__main__':
    unittest.main()