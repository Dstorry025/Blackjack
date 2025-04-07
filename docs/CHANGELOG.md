# CHANGELOG

## [Unreleased]
### Added
- Initial project structure with separate modules for game logic, UI, modes, and utilities.
- Command-line interface (CLI) for player interaction.
- Graphical user interface (GUI) for enhanced user experience.
- Single-player mode for playing against the dealer.
- Multiplayer mode for competitive play among multiple players.
- Tournament mode for series play with prizes.

### Changed
- Improved game logic in `blackjack.py` to handle various game states and betting rules.
- Enhanced dealer behavior in `dealer.py` to follow standard blackjack rules.
- Updated card handling in `deck.py` to include shuffling and drawing mechanics.
- Refined player actions and attributes in `player.py` for better gameplay experience.
- Improved hand value calculations in `hand.py` to account for blackjack rules.

### Fixed
- Resolved issues with card representation in `card.py`.
- Fixed bugs in the UI components to ensure smooth interaction.
- Addressed edge cases in game logic that could lead to incorrect outcomes.

## [0.1.0] - 2023-10-01
### Added
- Basic game mechanics for blackjack.
- Initial implementation of the dealer and player classes.
- Basic CLI for starting the game and placing bets.

### Changed
- Refactored code for better readability and maintainability.

### Fixed
- Minor bugs in the initial game logic.