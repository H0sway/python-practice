# Control Flow Notes

# If statements: These are similar to ruby, use if to start, elif for other
# options, and else for the catch all

# While statements let you keep code running until you tell it to stop. One
# good way of doing this is to set the parameter to a variable defined as
# "True" and then set it to false within the function when you want it to stop.

# Example:

# import random because I want to have it be more of a game than to set the
# same answer every time
import random

def guess_number():
    #define the number to be guessed and have it be random between 1 and 10
    number = random.randint(1,10)
    # Set the condition for the while loop
    running = True

    # While the program is running, guess a number between 1 and 10. Should
    # give feedback as to whether or not that number is too high or too low
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
    # End the loop
    else:
        print("The guessing game is now over.")
# Call the function
guess_number()

# For Loops: iterates over a sequence of objects. Basically it executes code
# for each value for 'i'. The else statement is optional, it will always be
# executed after the for loop completes. Use it when you want something else to
# happen when it finishes.

# Example:

# Loops over the numbers 1-5 and prints them out.
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')

# Break: Used to stop loops (for, while) before they normally would. When this
# happens the else statement (if exists) wont be executed.

# Example:

# While true, input in a string and it'll count the number of characters in the
# string. If you type in quit it will quit out of the loop.
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')

# Continue: Used to skip the rest of the statements in the current loop and
# move on to the next iteration of that loop. Works with both for and while
# loops

# Example:

# While true, input a string. If the string is less than three characters don't
# process it. If not, skip the rest of the statements.
while True:
    s = input("Enter something : ")

    if s = 'quit':
        break
    if len(s) < 3:
        print("Too small dude.")
        continue
    print('Input is of sufficient length')
