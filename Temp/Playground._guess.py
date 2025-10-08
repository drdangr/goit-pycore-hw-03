import random

attempts = 5
number = random.randint(1, 20)

try:
    guess = int(input("Guess a number between 1 and 20: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

while attempts > 1:
    if guess < 1 or guess > 20:
        print("Your guess is out of bounds. Please guess a number between 1 and 20.")
    elif guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Congratulations! You've guessed the number!")
        break

    attempts -= 1
    print(f"You have {attempts} attempts left.")
    
    try:
        guess = int(input("Try again: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        exit()  
