import random

player = random.randint(1, 6)
computer = random.randint(1, 6)

print("You rolled:", player)
print("Computer rolled:", computer)

if player > computer:
    print("You win!")
elif player < computer:
    print("Computer wins!")
else:
    print("Draw!")
