"""Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they 
guessed too low, too high, or exactly right. 
(_Hint: remember to use the user input lessons from the very 
 first exercise

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when 
the game ends, print this out."""

import random

number = random.randint(1,9)
count = 0
guess = 0
while guess!=number and guess!="exit":
    guess = input("enter your guess : ")
    if guess == "exit":
        break
    guess = int(guess)
    count+=1
    if guess>number:
        print("TOO HIGH !")
    elif guess<number:
        print("TOO LOW !")
    else:
        print("You got number.")
        print("it took you ",count," tries")
        