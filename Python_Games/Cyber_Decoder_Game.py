import base64

secret = "SGVsbG8gZnJvbSBQeXRob24h"

answer = input("Decode this Base64 text: " + secret + "\nYour answer: ")

decoded = base64.b64decode(secret).decode()

if answer == decoded:
    print("Correct!")
else:
    print("Wrong. The answer was:", decoded)
