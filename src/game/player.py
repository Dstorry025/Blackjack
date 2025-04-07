class Player:
    def __init__(self, name, bankroll):
        self.name = name
        self.bankroll = bankroll
        self.bet = 0
        self.hand = Hand()
        self.split_hands = []

    def place_bet(self, amount):
        if amount > self.bankroll:
            raise ValueError("Bet exceeds bankroll.")
        self.bet = amount
        self.bankroll -= amount

    def win_bet(self):
        self.bankroll += self.bet * 2  # Win pays 2:1
        self.bet = 0

    def push_bet(self):
        self.bankroll += self.bet  # Return bet on a push
        self.bet = 0

    def is_bust(self):
        return self.hand.value() > 21

    def split_hand(self):
        if len(self.hand.cards) == 2 and self.hand.cards[0].face == self.hand.cards[1].face:
            new_hand = Hand()
            new_hand.cards.append(self.hand.cards.pop())
            self.split_hands.append(new_hand)
            self.bankroll -= self.bet  # Deduct bet for the new hand
            return True
        return False

    def reset_hand(self):
        self.hand = Hand()
        self.split_hands = []

    def __str__(self):
        return f"{self.name} - Bankroll: ${self.bankroll}, Bet: ${self.bet}"