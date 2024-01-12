from random import randint

number = randint(1, 10)
print(number)
guess_num = None

while guess_num != number:
    guess_num = int(input("What is your guess number from 1 - 10? "))
    if guess_num > number:
        print("TOO HIGH")
    elif guess_num < number:
        print("TOO LOW")
    else:
        print("YOU WIN")
        # play_again = input("Do you want to play again? Y/ N ").lower()
        # if play_again == "y":
        #     number = randint(1, 10)
        #     print(number)
        #     guess_num = None
        # elif play_again == "n":
        #     print("Bye")
        # else:
        while True:
            play_again = input("Do you want to play again? Y/ N ").lower()
            if play_again == "y":
                number = randint(1, 10)
                print(number)
                guess_num = None
                break
            elif play_again == "n":
                print("Bye")
                break







        

