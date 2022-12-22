from random import randint


def guess_the_number(x):
    random_number = randint(1, x)
    guess_the_number = 0
    while random_number != guess_the_number:
        guess_the_number = int(input("Guess the number: "))
        if guess_the_number > random_number:
            print("The number is too big.")
        elif guess_the_number < random_number:
            print("The number is too low.")
    print("You guessed the right number.")
number = int(input("Enter the max number: "))
guess_the_number(number)
