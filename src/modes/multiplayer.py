from game import Game
from player import Player
from deck import Deck
from hand import Hand
import random

class MultiplayerGame:
    def __init__(self, player_names):
        self.players = [Player(name, 500) for name in player_names]  # Initialize players with a default bankroll
        self.dealer = Player("Dealer", 0)  # Dealer does not have a bankroll
        self.deck = Deck()
        self.current_player_index = 0

    def start_round(self):
        self.deck = Deck()  # Reset the deck for a new round
        for player in self.players:
            player.hand = Hand()  # Reset hands for all players
        self.dealer.hand = Hand()  # Reset dealer's hand
        self.deal_initial_cards()

    def deal_initial_cards(self):
        for _ in range(2):
            for player in self.players:
                player.hand.cards.append(self.deck.draw())
            self.dealer.hand.cards.append(self.deck.draw())

    def player_turn(self):
        current_player = self.players[self.current_player_index]
        while True:
            action = self.get_player_action(current_player)
            if action == "hit":
                current_player.hand.cards.append(self.deck.draw())
                if current_player.is_bust():
                    print(f"{current_player.name} busted!")
                    break
            elif action == "stand":
                break
            elif action == "double":
                if current_player.bankroll >= current_player.bet:
                    current_player.bankroll -= current_player.bet
                    current_player.bet *= 2
                    current_player.hand.cards.append(self.deck.draw())
                    if current_player.is_bust():
                        print(f"{current_player.name} busted after doubling!")
                break

        self.current_player_index += 1
        if self.current_player_index >= len(self.players):
            self.dealer_turn()

    def dealer_turn(self):
        while self.dealer.should_hit():
            self.dealer.hand.cards.append(self.deck.draw())
        self.evaluate_results()

    def evaluate_results(self):
        dealer_value = self.dealer.hand.value()
        for player in self.players:
            player_value = player.hand.value()
            if player_value > 21:
                print(f"{player.name} loses! (Busted)")
            elif dealer_value > 21 or player_value > dealer_value:
                print(f"{player.name} wins!")
                player.bankroll += player.bet * 2
            elif player_value < dealer_value:
                print(f"{player.name} loses!")
            else:
                print(f"{player.name} pushes!")

    def get_player_action(self, player):
        # Placeholder for getting player action (hit, stand, double)
        # In a real implementation, this would involve user input
        return random.choice(["hit", "stand"])  # Random action for demonstration

if __name__ == "__main__":
    player_names = ["Alice", "Bob", "Charlie"]  # Example player names
    game = MultiplayerGame(player_names)
    game.start_round()
    while game.current_player_index < len(game.players):
        game.player_turn()