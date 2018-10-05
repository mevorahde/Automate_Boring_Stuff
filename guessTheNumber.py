# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 13:35:27 2018

@author: David E
"""

# This is a guess the number game.
# Excerise in Chapter 3 of the 'Automate the Boring Stuff in Python' book.
import random
secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20.")

#Ask the player to guess 6 times
for guessesTaken in range(1,7):
    print("Take a guess.")
    guess = int(input())
    
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break # This condition is the correct guess
    
if guess == secretNumber:
    print("Goob Job! You gussed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))