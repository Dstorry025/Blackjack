import unittest
from game.card import Card

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card("Ace", "Hearts")

    def test_card_initialization(self):
        self.assertEqual(self.card.face, "Ace")
        self.assertEqual(self.card.suit, "Hearts")

    def test_card_string_representation(self):
        self.assertEqual(str(self.card), "Ace of Hearts")

    def test_card_face_value(self):
        face_values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10,
            "Ace": 11
        }
        for face, value in face_values.items():
            card = Card(face, "Diamonds")
            self.assertEqual(card.value(), value)

if __name__ == "__main__":
    unittest.main()