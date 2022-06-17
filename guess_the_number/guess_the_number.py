# Guess the Number

import random

def play(a, b, diff):
    """Play a round using the provided parameters."""
    # chooses the random number
    secret_num = random.randint(a, b + 1)

    lives = diff
    is_game_over = False
    victory = False

    while not is_game_over:
        if lives == 1:
            print(f"You have {lives} attempt remaining to guess the number.")
        else:
            print(f"You have {lives} attempts remaining to guess the number.")
        guess = get_integer(a, b)

        # evaluate the guess
        if guess == secret_num:
            victory = True
            is_game_over = True
            print(f"You are correct! The number was {secret_num}.")
        elif guess > secret_num:
            lives -= 1
            print("That's too high!")
        elif guess < secret_num:
            lives -= 1
            print("That's too low!")

        if lives == 0:
            is_game_over = True
            print("No more attempts left.")

    # prints the result
    if victory:
        print("\nYou win!\n")
    else:
        print("\nYou lose.\n")


def choose_difficulty(att_dict):
    """Takes a dictionary and returns the key chosen by the user."""

    choices_list = []

    for key in att_dict:
        choices_list.append(f"\"{key}\"")
    print(f"Choose a difficulty. Type {' or '.join(choices_list)}:")

    # making sure the user chooses a valid option
    while True:
        diff_choice = input("> ").lower()
        if diff_choice in att_dict:
            break
        print(f"Invalid option. Please choose {' or '.join(choices_list)}.")
    return att_dict[diff_choice]


def get_integer(a, b):
    """Asks the user to input a number from the provided range, and returns an integer."""
    print("Make a guess:")
    while True:
        guess_str = input("> ")
        # make sure it's a valid choice
        try:
            guess_int = int(guess_str)
            if not (a <= guess_int <= b):
                print(f"Please enter an integer between {a} and {b}.")
            else:
                return guess_int
        except ValueError:
            print("Please enter an integer.")


# main loop
while True:
    num_from = -50
    num_to = 50
    attempts_dict = {
        "easy": 10,
        "hard": 5,
        "extreme": 3,
    }

    print("Welcome to the Number Guessing Game!\n")
    print(f"I'm thinking of a number between {num_from} and {num_to}.")

    attempts = choose_difficulty(attempts_dict)

    # play a round with the specific parameters
    play(num_from, num_to, attempts)

    print("Enter \"y\" to play again, or anything else to quit.")
    quit_choice = input("> ")
    if quit_choice != "y":
        break
    print("\n" * 2)

print("Thanks for playing!")
