class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(face, suit) for suit in suits for face in faces]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop()
        return None

    def reset(self):
        self.__init__()  # Reinitialize the deck to reset it

    def remaining_cards(self):
        return len(self.cards)