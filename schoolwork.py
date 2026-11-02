
import random

number = random.randint(1, 20)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number (1-20): "))
        attempts += 1

        if guess == number:
            print(f"Correct! You took {attempts} attempts.")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

    except ValueError:
        print("Invalid input! Enter a whole number.")
