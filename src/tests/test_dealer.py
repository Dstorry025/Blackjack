import unittest
from game.dealer import Dealer
from game.card import Card
from game.hand import Hand

class TestDealer(unittest.TestCase):

    def setUp(self):
        self.dealer = Dealer()

    def test_initial_hand(self):
        self.assertIsInstance(self.dealer.hand, Hand)
        self.assertEqual(len(self.dealer.hand.cards), 0)

    def test_should_hit(self):
        # Test when dealer's hand value is less than 17
        self.dealer.hand.cards = [Card('5', 'Hearts'), Card('9', 'Diamonds')]
        self.assertTrue(self.dealer.should_hit())

        # Test when dealer's hand value is exactly 17
        self.dealer.hand.cards = [Card('10', 'Hearts'), Card('7', 'Diamonds')]
        self.assertFalse(self.dealer.should_hit())

        # Test when dealer's hand value is greater than 17
        self.dealer.hand.cards = [Card('10', 'Hearts'), Card('8', 'Diamonds')]
        self.assertFalse(self.dealer.should_hit())

    def test_is_bust(self):
        # Test when dealer's hand value is less than or equal to 21
        self.dealer.hand.cards = [Card('10', 'Hearts'), Card('8', 'Diamonds')]
        self.assertFalse(self.dealer.is_bust())

        # Test when dealer's hand value exceeds 21
        self.dealer.hand.cards = [Card('10', 'Hearts'), Card('9', 'Diamonds'), Card('3', 'Clubs')]
        self.assertTrue(self.dealer.is_bust())

if __name__ == '__main__':
    unittest.main()