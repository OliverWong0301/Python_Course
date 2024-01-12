# import random
from random import randint # then the code below you don't have to repeat random. before randint(0,2)

print("WELCOME TO PAPER, ROCK AND SCISSORS GAME")

player_scores = 0
computer_scores = 0

player = input("What is your name player? ")

while player_scores <= 3 or computer_scores <= 3:

    random_num = randint(0, 2)

    if random_num == 0:
        computer = "rock"
    elif random_num == 1:
        computer = "scissors"
    else:
        computer = "paper" 

    player_move = input(f"{player}, make your move: ").lower() # .lower() is a function that will bring back every letter from upper to lowercase

    print(f"Computer: {computer}")

    if player_move:
        if (player_move == "rock" and computer == "scissors") or (player_move == "scissors" and computer == "paper") or (player_move == "paper" and computer == "rock"):
            print("Player " + player + " wins \U0001f600")
            player_scores += 1
            print(f"Player scores: {player_scores} vs Computer scores: {computer_scores}")
            if player_scores == 3:
                print("Player wins finally" + (" \U0001f600" * 10))
                break

            elif (computer == "rock" and player_move == "scissors") or (computer == "scissors" and player_move == "paper") or (computer == "paper" and player_move == "rock"):
                print("Computer wins \U0001F923")
                computer_scores += 1
                print(f"Player scores: {player_scores} vs Computer scores: {computer_scores}")
                if computer_scores == 3:
                    print("Computer wins finally" + (" \U0001F923" * 10) + f"\n{player} MUST DRINK")
                    break

            elif player_move == computer:
                print("Both players tie")
                print(f"Player scores: {player_scores} vs Computer scores: {computer_scores}")

            elif (player_move == "lon") or (player_move == "cac") or (player_move == "dm") or (player_move == "du ma"):
                print("You little son of the bitch!!!")
                
            else:
                print("Must be rock, scissors, paper. Otherwise the game won't start")
                
    else:
            print("You didn't make any move")

            