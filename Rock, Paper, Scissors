from random import choice

while True:
    user = input("r for rock, p for paper and s for scissors: ")
    computer = choice(["r", "p", "s"])
    if user == computer:
        print("its a tie")
    elif user == "r" and computer == "s" or user == "s" and computer == "p" or user == "p" and computer == "r":
        print("you win")
    elif computer == "r" and user == "s" or computer == "s" and user == "p" or computer == "p" and user == "r":
        print("you lose")
    else:
        print("wrong input")
    try_again = input("Do you want to play again? y for yes, n for no")
    if try_again.capitalize() == "Y":
        continue
    elif try_again.capitalize() == "N":
        break
    else:
        print("invalid input")
        print("good bye")
