from game import Game
from player import Player

class Tournament:
    def __init__(self, players, buy_in):
        self.players = players
        self.buy_in = buy_in
        self.pot = 0
        self.rounds = []

    def start_tournament(self):
        for player in self.players:
            player.bankroll -= self.buy_in
            self.pot += self.buy_in
        self.play_rounds()

    def play_rounds(self):
        while len(self.players) > 1:
            round_result = self.play_round()
            self.rounds.append(round_result)
            self.eliminate_players()
        self.declare_winner()

    def play_round(self):
        game = Game()
        game.start_round()
        # Implement round logic here, returning results for the round
        return game.end_round()

    def eliminate_players(self):
        self.players = [player for player in self.players if player.bankroll > 0]

    def declare_winner(self):
        if self.players:
            winner = self.players[0]
            winner.bankroll += self.pot
            print(f"{winner.name} wins the tournament and takes home ${self.pot}!")
        else:
            print("No players left in the tournament.")

# Example usage
if __name__ == "__main__":
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    tournament = Tournament([player1, player2], 100)
    tournament.start_tournament()