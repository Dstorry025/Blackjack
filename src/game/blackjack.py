from .dealer import Dealer
from .deck import Deck

class Blackjack:
    def __init__(self):
        self.players = []
        self.dealer = Dealer()
        self.deck = Deck()
        self.current_bet = 0
        self.round_over = True

    def add_player(self, player):
        self.players.append(player)

    def start_round(self):
        self.round_over = False
        self.current_bet = 0
        self.deck.shuffle()
        self.dealer.hand.clear()
        for player in self.players:
            player.hand.clear()
            player.reset_bet()

        self.deal_initial_cards()

    def deal_initial_cards(self):
        for _ in range(2):
            for player in self.players:
                player.hand.add_card(self.deck.draw())
            self.dealer.hand.add_card(self.deck.draw())

    def place_bet(self, player, amount):
        if player.bankroll >= amount:
            player.bankroll -= amount
            player.current_bet += amount
            self.current_bet += amount
        else:
            raise ValueError("Insufficient funds to place bet.")

    def player_turn(self, player):
        while not self.round_over:
            action = player.choose_action()
            if action == 'hit':
                player.hand.add_card(self.deck.draw())
                if player.hand.value() > 21:
                    player.bust()
                    break
            elif action == 'stand':
                break
            elif action == 'double':
                self.place_bet(player, player.current_bet)
                player.hand.add_card(self.deck.draw())
                if player.hand.value() > 21:
                    player.bust()
                break

    def dealer_turn(self):
        while self.dealer.should_hit():
            self.dealer.hand.add_card(self.deck.draw())

    def evaluate_round(self):
        dealer_value = self.dealer.hand.value()
        for player in self.players:
            player_value = player.hand.value()
            if player_value > 21:
                player.bust()
            elif dealer_value > 21 or player_value > dealer_value:
                player.win(self.current_bet)
            elif player_value < dealer_value:
                player.lose()
            else:
                player.push()

        self.round_over = True

    def reset_game(self):
        for player in self.players:
            player.reset()
        self.dealer.reset()
        self.deck.reset()