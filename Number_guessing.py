import random

Easy_level = 6
Hard_level = 3

def level_choosen(level):
    if level == 'Easy':
        return Easy_level
    else:
        return Hard_level

def check_ans(guess_number, number, attempts):
    if guess_number < number:
        print("Your number is too low.")
        return attempts - 1, False
    elif guess_number > number:
        print("Your guess is too high.")
        return attempts - 1, False
    else:
        print(f"Your guess is right! The number was {number}.")
        return attempts, True

print("Welcome to the Number Guessing Game!")
print(" a number between 1 and 100.")

number = random.randint(1, 100)

level = input("Choose a difficulty. Type 'Easy' or 'Hard': ").strip().capitalize()
while level not in ['Easy', 'Hard']:
    level = input("Invalid choice. Please type 'Easy' or 'Hard': ").strip().capitalize()

attempts = level_choosen(level)
guess_number = 0
flag = False

while guess_number != number and attempts > 0:
    print(f"\nYou have {attempts} attempts remaining to guess the number.")
    try:
        guess_number = int(input("Make a guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    attempts, flag = check_ans(guess_number, number, attempts)

    if flag:
        break
    elif attempts == 0:
        print("You've run out of attempts. You lose!")
    else:
        print("Guess again.")

