import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("=" * 40)
print("🎮 Welcome to Guess the Number!")
print("I have selected a number between 1 and 100.")
print("Can you guess it?")
print("=" * 40)

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print("\n Congratulations!")
        print(f"You guessed the number {secret_number} correctly!")
        print(f"It took you {attempts} attempts.")
        break