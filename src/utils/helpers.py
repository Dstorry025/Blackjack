def calculate_bet(bankroll, bet_amount):
    """Calculate the remaining bankroll after placing a bet."""
    if bet_amount > bankroll:
        raise ValueError("Bet amount exceeds bankroll.")
    return bankroll - bet_amount

def format_card(card):
    """Format a card for display."""
    return f"{card.face} of {card.suit}"

def display_hand(hand):
    """Display the cards in a hand."""
    return ', '.join(format_card(card) for card in hand.cards)

def is_valid_bet(bet_amount, bankroll):
    """Check if the bet amount is valid."""
    return 0 < bet_amount <= bankroll

def get_winner(player_value, dealer_value):
    """Determine the winner between player and dealer."""
    if player_value > 21:
        return "Dealer"
    elif dealer_value > 21 or player_value > dealer_value:
        return "Player"
    elif player_value < dealer_value:
        return "Dealer"
    else:
        return "Push"  # Tie situation