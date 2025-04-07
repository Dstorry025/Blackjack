import sys
from game.blackjack import Blackjack
from ui.cli import CLI
from ui.gui import GUI

def main():
    game_mode = input("Choose game mode (1: CLI, 2: GUI): ")
    
    if game_mode == '1':
        cli = CLI()
        cli.start()
    elif game_mode == '2':
        gui = GUI()
        gui.start()
    else:
        print("Invalid choice. Exiting...")
        sys.exit(1)

if __name__ == "__main__":
    main()