import random

print("🔐 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20...")

secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess = input("Take a guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"🎉 You got it in {attempts} attempts! The number was {secret_number}.")
        break
