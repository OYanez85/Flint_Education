import time

sentence = "Python is a great language for beginners."

input("Press Enter when ready...")
start = time.time()

typed = input("Type this sentence:\n" + sentence + "\n")

end = time.time()
time_taken = round(end - start, 2)

if typed == sentence:
    print("Correct!")
else:
    print("You made mistakes.")

print("Time:", time_taken, "seconds")
