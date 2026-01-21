import random

guess = None
random_number = random.randint(1, 100)
number_of_guesses = 0

while guess != random_number:
    guess = int(input("Enter a number: "))
    number_of_guesses += 1
    if guess == random_number:
        print(f"You guesses it right the number was {random_number}")
    elif guess > random_number:
        print("Enter a Lower number")
    elif guess < random_number:
        print("Enter a Higher number")
        

print("Congratulation")
print(f"You took {number_of_guesses} attempts to guess the number.")