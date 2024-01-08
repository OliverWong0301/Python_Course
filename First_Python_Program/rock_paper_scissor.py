print("WELCOME TO ROCK, PAPER, SCISSORS GAME")

player1 = input("Player 1, please make your move: ")
print("*** NO CHEATING \n\n" * 15)
player2 = input("Player 2, please make your move: ")

if player1 and player2:
    if (player1 == "rock" and player2 == "paper") or (player1 == "paper" and player2 == "scissors") or (player1 == "scissors" and player2 == "rock"):
        print("Player2 wins")
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
        print("Player1 wins")
    elif player1 == player2:
        print("It's a tie for both!!!")
    elif ((player1 == "cac") or (player1 =="lon") or (player1 == "dm")) or ((player2 == "cac") or (player2 =="lon") or (player2 == "dm")):
        print("Fuck you bitch!!!")
    else: 
        print("Must be rock, paper, scissors and lowercase")
else:
    print("You didn't make any move!!!")