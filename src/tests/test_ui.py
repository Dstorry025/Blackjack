import unittest
from ui.gui import BlackjackGUI
from tkinter import Tk

class TestBlackjackGUI(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = BlackjackGUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initial_bankroll_display(self):
        self.app.bankroll_label.config(text="Bankroll: $500")
        self.assertEqual(self.app.bankroll_label.cget("text"), "Bankroll: $500")

    def test_bet_display(self):
        self.app.place_bet(50)
        self.assertEqual(self.app.bet_display.cget("text"), "Bet: $50")

    def test_rebet_functionality(self):
        self.app.place_bet(100)
        self.app.rebet()
        self.assertEqual(self.app.bet_display.cget("text"), "Bet: $100")

    def test_action_buttons_initial_state(self):
        self.assertEqual(self.app.hit_button['state'], 'disabled')
        self.assertEqual(self.app.stand_button['state'], 'disabled')
        self.assertEqual(self.app.double_button['state'], 'disabled')

    def test_action_buttons_state_after_deal(self):
        self.app.place_bet(50)
        self.app.start_round()
        self.assertEqual(self.app.hit_button['state'], 'normal')
        self.assertEqual(self.app.stand_button['state'], 'normal')
        self.assertEqual(self.app.double_button['state'], 'normal')

    def test_message_display(self):
        self.app.display_message("Test message")
        self.assertEqual(self.app.message_label.cget("text"), "Test message")

if __name__ == "__main__":
    unittest.main()