# import random
from random import randint # then the code below you don't have to repeat random. before randint(0,2)

random_num = randint(0, 2) 

print("WELCOME TO PAPER, ROCK AND SCISSORS GAME")
player = input("What is your name player? ")
print(f"Now, {player} please make your move: ")
player_move = input(f"{player}: ").lower() # .lower() is a function that will bring back every letter from upper to lowercase

if random_num == 0:
    computer = "rock"
elif random_num == 1:
    computer = "scissors"
else:
    computer = "paper"
print(f"Computer: {computer}")

if player_move:
    if (player_move == "rock" and computer == "scissors") or (player_move == "scissors" and computer == "paper") or (player_move == "paper" and computer == "rock"):
        print("Player " + player + " wins")
    elif (computer == "rock" and player_move == "scissors") or (computer == "scissors" and player_move == "paper") or (computer == "paper" and player_move == "rock"):
        print("Computer wins")
    elif player_move == computer:
        print("Both players tie")
    elif (player_move == "lon") or (player_move == "cac") or (player_move == "dm") or (player_move == "du ma"):
        print("You little son of the bitch!!!")
    else:
        print("Must be rock, scissors, paper. Otherwise the game won't start")
else:
    print("You didn't make any move")
