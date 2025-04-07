# API Documentation for Blackjack Game

## Overview

This document provides an overview of the API for the Blackjack game project. It includes descriptions of the main classes and methods available in the game, allowing developers to understand how to interact with the game's components programmatically.

## Classes

### Card

Represents a single playing card.

#### Methods

- `__init__(face: str, suit: str)`: Initializes a card with a face value and suit.

### Hand

Manages a collection of cards and calculates the hand's value.

#### Methods

- `__init__()`: Initializes an empty hand.
- `value() -> int`: Calculates and returns the total value of the hand.

### Deck

Manages the deck of cards, including shuffling and drawing.

#### Methods

- `__init__()`: Initializes a standard deck of 52 cards and shuffles them.
- `draw() -> Card`: Draws a card from the deck.

### Player

Represents a player in the game, managing their attributes and actions.

#### Methods

- `__init__(name: str, bankroll: int)`: Initializes a player with a name and bankroll.
- `is_bust() -> bool`: Checks if the player's hand value exceeds 21.
- `split_hand() -> bool`: Splits the player's hand if they have a pair.

### Dealer

Represents the dealer in the game, managing the dealer's hand and actions.

#### Methods

- `__init__()`: Initializes the dealer with a hand.
- `should_hit() -> bool`: Determines if the dealer should hit based on their hand value.
- `is_bust() -> bool`: Checks if the dealer's hand value exceeds 21.

### Blackjack

Contains the main game logic, including rules for gameplay and managing game states.

#### Methods

- `start_game()`: Initializes and starts the game.
- `end_game()`: Ends the current game session and evaluates results.

## User Interface

### CLI

- `src/ui/cli.py`: Implements a command-line interface for player interactions.

### GUI

- `src/ui/gui.py`: Implements a graphical user interface for a more engaging experience.

## Game Modes

### Single Player

- `src/modes/single_player.py`: Allows a player to play against the dealer.

### Multiplayer

- `src/modes/multiplayer.py`: Enables multiple players to compete against each other.

### Tournament

- `src/modes/tournament.py`: Implements a tournament mode for players to compete in a series of games.

## Utilities

### Logger

- `src/utils/logger.py`: Provides logging functionality for tracking events and errors.

### Helpers

- `src/utils/helpers.py`: Contains utility functions for various tasks throughout the application.

### Configuration

- `src/utils/config.py`: Manages configuration settings for the game.

## Testing

The project includes a comprehensive suite of tests located in the `src/tests` directory, covering all major components of the game to ensure functionality and reliability.

## Contribution

For guidelines on contributing to the project, please refer to the `CONTRIBUTING.md` file in the `docs` directory.