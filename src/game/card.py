class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        return f"{self.face} of {self.suit}"

    def value(self):
        if self.face in ['Jack', 'Queen', 'King']:
            return 10
        elif self.face == 'Ace':
            return 11  # Aces are initially worth 11
        else:
            return int(self.face)  # Numeric cards are converted to integers

    def is_ace(self):
        return self.face == 'Ace'