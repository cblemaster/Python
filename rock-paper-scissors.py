import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Choose rock, paper, or scissors...\n")

print("Computer chooses: ", computer_choice)
print("Player chooses: ", user_choice)

tie = computer_choice == user_choice
player_win = (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper" )

if tie:
    print("Tie!")
elif player_win:
    print("YOU WIN!!")
else:
    print("Sorry, you lose :()")
