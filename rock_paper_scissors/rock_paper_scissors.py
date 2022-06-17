# Rock Paper Scissors

import random


rock = 'rock'

paper = 'paper'

scissors = 'scissors'

# putting them into a list for easier access
choices = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

# making sure the input is valid
options = ["0", "1", "2"]
while True:
    player_choice_str = input("> ")
    if player_choice_str not in options:
        print("Invalid choice. Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    else:
        break

# changing the data type
player_choice = int(player_choice_str)
print("You chose:")
print(choices[player_choice])

# computer's choice
comp_choice = random.randint(0, 2)
print("Computer chose:")
print(choices[comp_choice])

# evaluating the result
# tie
if player_choice == comp_choice:
    print("It's a tie!")
    
# player wins: (rock and scissors) or (paper and rock) or (scissors and paper)
elif (player_choice == 0 and comp_choice == 2) or\
        (player_choice == 1 and comp_choice == 0) or\
        (player_choice == 2 and comp_choice == 1):
    print("You win!")
    
# computer wins
else:
    print("You lose.")
