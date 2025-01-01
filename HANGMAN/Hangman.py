import random

def hangman():
    """
    Plays a game of Hangman with a food-themed word list.
    """
    word_list = ["pizza", "burger", "sushi", "tacos", "pasta", "ice cream", "chocolate", "cake", "cookies", 
                "noodles", "burrito", "sandwich", "salad", "steak", "fruit", "vegetables", "popcorn"]
    word = random.choice(word_list)
    word_letters = set(word)  # Letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # What the user has guessed

    lives = 6

    # Get user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        print(f"You have {lives} lives left. Used letters: {' '.join(used_letters)}")

        # What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f"Current word: {' '.join(word_list)}")

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")

            else:
                lives -= 1  # Takes away a life if wrong
                print("\nNope, that letter's not in there.")

        elif user_letter in used_letters:
            print("\nYou already guessed that. Try again!")

        else:
            print("\nInvalid input. Please enter a single letter.")

    # Gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(f"You're out of lives! The word was '{word}'.")
    else:
        print(f"Congrats, you guessed it! The word was '{word}'.")

hangman()