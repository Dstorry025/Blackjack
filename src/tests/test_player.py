import unittest
from game.player import Player
from game.card import Card
from game.hand import Hand

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Test Player", 1000)

    def test_initial_attributes(self):
        self.assertEqual(self.player.name, "Test Player")
        self.assertEqual(self.player.bankroll, 1000)
        self.assertEqual(self.player.bet, 0)
        self.assertIsInstance(self.player.hand, Hand)

    def test_place_bet(self):
        self.player.place_bet(100)
        self.assertEqual(self.player.bet, 100)
        self.assertEqual(self.player.bankroll, 900)

    def test_bet_exceeds_bankroll(self):
        with self.assertRaises(ValueError):
            self.player.place_bet(1100)

    def test_win_bet(self):
        self.player.place_bet(100)
        self.player.win_bet()
        self.assertEqual(self.player.bankroll, 1100)

    def test_lose_bet(self):
        self.player.place_bet(100)
        self.player.lose_bet()
        self.assertEqual(self.player.bankroll, 900)

    def test_split_hand(self):
        card1 = Card("Ace", "Hearts")
        card2 = Card("Ace", "Diamonds")
        self.player.hand.cards.extend([card1, card2])
        self.assertTrue(self.player.split_hand())
        self.assertEqual(len(self.player.split_hands), 1)
        self.assertEqual(len(self.player.hand.cards), 1)

    def test_split_hand_invalid(self):
        card1 = Card("Ace", "Hearts")
        card2 = Card("King", "Diamonds")
        self.player.hand.cards.extend([card1, card2])
        self.assertFalse(self.player.split_hand())
        self.assertEqual(len(self.player.split_hands), 0)

if __name__ == "__main__":
    unittest.main()