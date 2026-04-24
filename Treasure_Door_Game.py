print("You find three doors: red, blue and green.")

door = input("Which door do you open? ").lower()

if door == "red":
    print("A dragon appears. Game over!")
elif door == "blue":
    print("You find treasure. You win!")
elif door == "green":
    print("You fall into a trap!")
else:
    print("That door does not exist.")
