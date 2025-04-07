from tkinter import Tk, Frame, Label, Button, messagebox
from game.blackjack import Game

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Game")
        self.root.geometry("800x600")
        self.root.configure(bg="green")

        self.game = Game()
        self.current_player = self.game.players[0]

        self.create_widgets()
        self.update_bankroll_display()

    def create_widgets(self):
        self.dealer_frame = Frame(self.root, bg="green")
        self.dealer_frame.pack(pady=20)

        self.player_frame = Frame(self.root, bg="green")
        self.player_frame.pack(pady=20)

        self.dealer_label = Label(self.dealer_frame, text="Dealer's Hand:", bg="green", fg="white", font=("Arial", 16))
        self.dealer_label.pack()

        self.player_label = Label(self.player_frame, text="Player's Hand:", bg="green", fg="white", font=("Arial", 16))
        self.player_label.pack()

        self.message_label = Label(self.root, text="", bg="green", fg="white", font=("Arial", 14))
        self.message_label.pack(pady=10)

        self.bet_frame = Frame(self.root, bg="green")
        self.bet_frame.pack(pady=20)

        self.bet_label = Label(self.bet_frame, text="Place Your Bet:", bg="green", fg="white", font=("Arial", 16))
        self.bet_label.grid(row=0, column=0, columnspan=3)

        self.bet_amount = 0
        self.bet_display = Label(self.bet_frame, text=f"Bet: ${self.bet_amount}", bg="green", fg="white", font=("Arial", 14))
        self.bet_display.grid(row=1, column=0, columnspan=3)

        self.chip_10 = Button(self.bet_frame, text="$10", command=lambda: self.place_bet(10), font=("Arial", 14), bg="blue", fg="white")
        self.chip_10.grid(row=2, column=0, padx=10)

        self.chip_50 = Button(self.bet_frame, text="$50", command=lambda: self.place_bet(50), font=("Arial", 14), bg="blue", fg="white")
        self.chip_50.grid(row=2, column=1, padx=10)

        self.chip_100 = Button(self.bet_frame, text="$100", command=lambda: self.place_bet(100), font=("Arial", 14), bg="blue", fg="white")
        self.chip_100.grid(row=2, column=2, padx=10)

        self.deal_button = Button(self.bet_frame, text="Deal", command=self.start_round, font=("Arial", 14), bg="green", fg="white")
        self.deal_button.grid(row=3, column=0, columnspan=3, pady=10)

        self.bankroll_label = Label(self.root, text="Bankroll: $500", bg="green", fg="white", font=("Arial", 16))
        self.bankroll_label.pack(pady=10)

    def update_bankroll_display(self):
        self.bankroll_label.config(text=f"Bankroll: ${self.current_player.bankroll}")

    def place_bet(self, amount):
        if self.current_player.bankroll >= amount:
            self.bet_amount += amount
            self.current_player.bankroll -= amount
            self.current_player.bet = self.bet_amount
            self.bet_display.config(text=f"Bet: ${self.bet_amount}")
            self.update_bankroll_display()
        else:
            messagebox.showwarning("Insufficient Funds", "Not enough bankroll to place this bet!")

    def start_round(self):
        if self.bet_amount > 0:
            self.game.start_round()
            self.update_game_state()
        else:
            messagebox.showwarning("No Bet", "Please place a bet before starting the round.")

    def update_game_state(self):
        # Logic to update the GUI with the current game state
        pass

if __name__ == "__main__":
    root = Tk()
    app = BlackjackGUI(root)
    root.mainloop()