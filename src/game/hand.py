class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        total = 0
        aces = 0
        for card in self.cards:
            if card.face in ['Jack', 'Queen', 'King']:
                total += 10
            elif card.face == 'Ace':
                total += 11
                aces += 1
            else:
                total += int(card.face)

        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def is_bust(self):
        return self.value() > 21

    def clear(self):
        self.cards = []

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)