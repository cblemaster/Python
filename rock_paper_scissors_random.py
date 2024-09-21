
import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
player_choice = input("Do you want - rock, paper, or scissors?\n")

print('Computer choice:', computer_choice)
print('Player choice:', player_choice)

if computer_choice == player_choice:
    print('TIE')
elif player_choice == 'rock' and computer_choice == 'scissors':
    print('WIN')
elif player_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
elif player_choice == 'scissors' and computer_choice == 'paper':
    print('WIN')
else:
    print('You lose :( Computer wins :D')
