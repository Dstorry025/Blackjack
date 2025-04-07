import unittest
from game.blackjack import Game
from game.player import Player
from game.dealer import Dealer
from game.deck import Deck

class TestBlackjack(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.player = Player("Test Player", 1000)
        self.dealer = Dealer()
        self.game.players.append(self.player)

    def test_initial_bankroll(self):
        self.assertEqual(self.player.bankroll, 1000)

    def test_place_bet(self):
        self.player.place_bet(100)
        self.assertEqual(self.player.bet, 100)
        self.assertEqual(self.player.bankroll, 900)

    def test_dealer_should_hit(self):
        self.dealer.hand.cards = [Card('10', 'Hearts'), Card('5', 'Diamonds')]
        self.assertTrue(self.dealer.should_hit())

    def test_dealer_should_stand(self):
        self.dealer.hand.cards = [Card('10', 'Hearts'), Card('8', 'Diamonds')]
        self.assertFalse(self.dealer.should_hit())

    def test_player_bust(self):
        self.player.hand.cards = [Card('10', 'Hearts'), Card('9', 'Diamonds'), Card('3', 'Clubs')]
        self.assertTrue(self.player.is_bust())

    def test_player_blackjack(self):
        self.player.hand.cards = [Card('Ace', 'Hearts'), Card('10', 'Diamonds')]
        self.assertEqual(self.player.hand.value(), 21)

    def test_deck_draw(self):
        deck = Deck()
        initial_count = len(deck.cards)
        card = deck.draw()
        self.assertIsNotNone(card)
        self.assertEqual(len(deck.cards), initial_count - 1)

    def test_game_round(self):
        self.game.start_round()
        self.assertEqual(len(self.player.hand.cards), 2)
        self.assertEqual(len(self.dealer.hand.cards), 2)

if __name__ == '__main__':
    unittest.main()