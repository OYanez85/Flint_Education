score = 0

questions = {
    "What command lists files in Linux? ": "ls",
    "What language uses print()? ": "python",
    "What does CPU stand for? ": "central processing unit"
}

for question, answer in questions.items():
    user = input(question).lower()

    if user == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Final score:", score, "/", len(questions))
