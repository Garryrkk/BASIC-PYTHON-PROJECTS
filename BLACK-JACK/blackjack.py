import random

# ... (rest of your original code: suits, ranking, card_val, Card, Hand, Deck classes) ...

# Global variables
playing = False
chip_pool = 100
bet = 0
dealer_hand = Hand()
player_hand = Hand()
deck = Deck()

def make_bet():
    """Asks the player for the bet amount and validates it."""
    global bet, chip_pool

    bet = 0
    while bet == 0:
        try:
            bet = int(input("What amount of chips would you like to bet? "))
            if 0 < bet <= chip_pool:
                break
            else:
                print(f"Invalid bet. You only have {chip_pool} remaining.")
        except ValueError:
            print("Please enter a valid integer.")

def deal_cards():
    """Deals out cards and sets up the round."""
    global playing, deck, player_hand, dealer_hand, chip_pool, bet

    deck = Deck()
    deck.shuffle()

    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    playing = True
    game_step()

def hit():
    """Handles the player's hit action."""
    global playing, chip_pool, deck, player_hand, dealer_hand

    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())

            if player_hand.calc_val() > 21:
                result = "Busted! You lose."
                chip_pool -= bet
                playing = False
        else:
            result = "You already busted."
    else:
        result = "Sorry, you can't hit."

    game_step()

def stand():
    """Handles the player's stand action."""
    global playing, chip_pool, deck, player_hand, dealer_hand

    if not playing:
        result = "Sorry, you can't stand."
    else:
        while dealer_hand.calc_val() < 17:
            dealer_hand.card_add(deck.deal())

        if dealer_hand.calc_val() > 21:
            result = "Dealer busts! You win!"
            chip_pool += bet
        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = "You beat the dealer! You win!"
            chip_pool += bet
        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = "Tied up, push!"
        else:
            result = "Dealer wins!"
            chip_pool -= bet

        playing = False
    game_step()

def game_step():
    """Displays the game state and prompts the player for input."""
    print("\nPlayer Hand:", player_hand)
    print("Player Hand Total:", player_hand.calc_val())
    print("\nDealer Hand:", dealer_hand.draw(hidden=True))

    if playing:
        print("Dealer Hand Total (Hidden): ???")
    else:
        print("Dealer Hand Total:", dealer_hand.calc_val())

    print("\nChip Total:", chip_pool)
    print(result)

    if playing:
        player_input()
    else:
        print("Press 'd' to deal again or 'q' to quit.")
        player_input()

def player_input():
    """Reads and validates player input."""
    plin = input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid Input. Enter 'h', 's', 'd', or 'q':")
        player_input()

def intro():
    """Displays the game introduction."""
    print("""
    Welcome to BlackJack! Get as close to 21 as you can without going over!
    Dealer hits until she reaches 17. Aces count as 1 or 11. 
    """)

if __name__ == "__main__":
    intro()
    deal_cards()