class Dealer:
    def __init__(self):
        self.hand = Hand()

    def should_hit(self):
        return self.hand.value() < 17

    def is_bust(self):
        return self.hand.value() > 21

    def reveal_hand(self):
        return self.hand.cards

    def clear_hand(self):
        self.hand = Hand()