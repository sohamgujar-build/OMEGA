import random
from tkinter import SE
secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == secret:
        print(f"You guessed it in {attempts} attempts!")
        break
    if guess< secret:
        print("Too low! Try again:")
    else:
        print("Too high! Try again:")





