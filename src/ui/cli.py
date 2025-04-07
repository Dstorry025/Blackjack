import sys
from game.blackjack import Game

class CLI:
    def __init__(self):
        self.game = Game()

    def display_welcome(self):
        print("====================================")
        print("            BLACKJACK              ")
        print("====================================")
        print("Welcome to the Blackjack game!")
        print("Type 'help' for a list of commands.")

    def display_help(self):
        print("Available commands:")
        print("  start - Start a new game")
        print("  bet <amount> - Place a bet")
        print("  hit - Take another card")
        print("  stand - End your turn")
        print("  double - Double your bet and take one more card")
        print("  quit - Exit the game")

    def start_game(self):
        self.game.start_round()
        self.display_game_state()

    def display_game_state(self):
        print("\nDealer's Hand:")
        print(self.game.dealer.hand)
        print("\nYour Hand:")
        print(self.game.player.hand)
        print(f"Your total: {self.game.player.hand.value()}")
        print(f"Dealer's total: {self.game.dealer.hand.value()}")

    def place_bet(self, amount):
        if self.game.player.bankroll >= amount:
            self.game.player.bet = amount
            self.game.player.bankroll -= amount
            print(f"You placed a bet of ${amount}.")
        else:
            print("Insufficient funds to place this bet.")

    def hit(self):
        self.game.player.hit()
        if self.game.player.is_bust():
            print("You busted! Game over.")
            self.end_game()

    def stand(self):
        self.game.dealer_turn()
        self.end_game()

    def double(self):
        if self.game.player.bankroll >= self.game.player.bet:
            self.game.player.bankroll -= self.game.player.bet
            self.game.player.bet *= 2
            self.game.player.hit()
            if self.game.player.is_bust():
                print("You busted! Game over.")
                self.end_game()
            else:
                self.game.dealer_turn()
                self.end_game()
        else:
            print("Insufficient funds to double your bet.")

    def end_game(self):
        print("Game over. Your final bankroll is: $", self.game.player.bankroll)
        sys.exit()

    def run(self):
        self.display_welcome()
        while True:
            command = input("> ").strip().lower()
            if command == "help":
                self.display_help()
            elif command == "start":
                self.start_game()
            elif command.startswith("bet"):
                try:
                    amount = int(command.split()[1])
                    self.place_bet(amount)
                except (IndexError, ValueError):
                    print("Usage: bet <amount>")
            elif command == "hit":
                self.hit()
            elif command == "stand":
                self.stand()
            elif command == "double":
                self.double()
            elif command == "quit":
                print("Thanks for playing!")
                break
            else:
                print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    cli = CLI()
    cli.run()