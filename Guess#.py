import random

number = random.randint(1, 100)

print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break
