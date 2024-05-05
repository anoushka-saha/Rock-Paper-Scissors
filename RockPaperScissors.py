#ANOUSHKA SAHA
#ROCK PAPER SCISSORS

import random

user_input = int(input(print("What do you choose? Type 1 for rock, 2 for paper, and 3 for scissors")))
comp_throw = random.randint(1,3)

if user_input == 1:
    if comp_throw == 1:
        print("Computer chose rock.")
        print("It's a tie.")
    elif comp_throw == 2:
        print("Computer chose paper.")
        print("You lose.")
    else:
        print("Computer chose scissors.")
        print("You win!")

if user_input == 2:
    if comp_throw == 1:
        print("Computer chose rock.")
        print("You win!")
    elif comp_throw == 2:
        print("Computer chose paper.")
        print("It's a tie.")
    else:
        print("Computer chose scissors.")
        print("You lose.")

if user_input == 3:
    if comp_throw == 1:
        print("Computer chose rock.")
        print("You lose")
    elif comp_throw == 2:
        print("Computer chose paper.")
        print("You win!")
    else:
        print("Computer chose scissors.")
        print("It's a tie.")