from game.blackjack import Blackjack
from game.player import Player
from game.dealer import Dealer
from game.deck import Deck
from game.hand import Hand
from ui.cli import CLI

class SinglePlayerMode:
    def __init__(self):
        self.player = None
        self.dealer = Dealer()
        self.deck = Deck()
        self.cli = CLI()

    def setup_game(self):
        player_name = self.cli.get_player_name()
        self.player = Player(player_name, bankroll=1000)  # Starting bankroll
        self.cli.display_welcome_message(player_name)

    def play_round(self):
        self.deck.shuffle()
        self.player.hand = Hand()
        self.dealer.hand = Hand()

        # Deal initial cards
        for _ in range(2):
            self.player.hand.add_card(self.deck.draw())
            self.dealer.hand.add_card(self.deck.draw())

        self.cli.display_hands(self.player, self.dealer, hide_dealer_card=True)

        # Player's turn
        while True:
            action = self.cli.get_player_action()
            if action == 'hit':
                self.player.hand.add_card(self.deck.draw())
                self.cli.display_hands(self.player, self.dealer, hide_dealer_card=True)
                if self.player.hand.value() > 21:
                    self.cli.display_bust_message(self.player)
                    return
            elif action == 'stand':
                break

        # Dealer's turn
        self.dealer_play()

        # Determine winner
        self.determine_winner()

    def dealer_play(self):
        while self.dealer.should_hit():
            self.dealer.hand.add_card(self.deck.draw())

    def determine_winner(self):
        player_value = self.player.hand.value()
        dealer_value = self.dealer.hand.value()

        self.cli.display_hands(self.player, self.dealer)

        if player_value > 21:
            self.cli.display_bust_message(self.player)
        elif dealer_value > 21 or player_value > dealer_value:
            self.cli.display_win_message(self.player)
        elif player_value < dealer_value:
            self.cli.display_loss_message(self.player)
        else:
            self.cli.display_push_message()

    def start_game(self):
        self.setup_game()
        while True:
            self.play_round()
            if not self.cli.play_again():
                break

if __name__ == "__main__":
    game_mode = SinglePlayerMode()
    game_mode.start_game()