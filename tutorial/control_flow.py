# Control Flow Notes

# If statements: These are similar to ruby, use if to start, elif for other
# options, and else for the catch all

# While statements let you keep code running until you tell it to stop. One
# good way of doing this is to set the parameter to a variable defined as
# "True" and then set it to false within the function when you want it to stop.

# Ex.
import random

def guess_number():
    number = random.randint(1,10)
    running = True

    while running:
        guess = int(input('Guess a number between 1 and 10 : '))

        if guess == number:
            print('Congratulations, you guessed the right number!')
            running = False
        elif guess < number:
            print("Nope, it's a little higher than that.")
        elif guess > number:
            print("Nope, it's a little lower than that.")
        else:
            print("Not entirely sure how we got here.", guess)
    else:
        print("The guessing game is now over.")

guess_number()
