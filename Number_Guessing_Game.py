import random

secret = random.randint(1, 20)
guess = 0

while guess != secret:
    guess = int(input("Guess a number from 1 to 20: "))

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You win!")
