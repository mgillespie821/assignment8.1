# This is a header for the application
# Megan Gillespie
# 7/27/2022
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time


def displayIntro():
  # This print statement has an excess of ''' at the beginning and end of the print statement on line 15.
    print('''You are in a land full of dragons. In front of you, 
	  you see two caves. In one cave, the dragon is friendly
	  and will share his treasure with you. The other dragon
	  is greedy and hungry, and will eat you on sight.''')
    print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return caves  # This is a spelling mistake of "caves", should be "cave"


def checkCave(chosenCave): # chosenCave is not defined, spelling mistake 
    print('You approach the cave...')
    # sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    # sleep for 2 seconds
    time.sleep(3) # this is sleeping for 3 seconds instead of 2 that is stated on line 36
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    # sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print
        'Gobbles you down in one bite!'  # missing parentheses to call print






# There is an excess of blank lines between line 49 and line 57


        +356 # logic error, not sure what is being incremented here


playAgain = 'yes'
# the operand is wrong should be == on line 63, invalid syntax
while playAgain = 'yes' or 'y':
    displayIntro()
    caveNumber = choosecave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)') #logic error, "no" is never defined
    playAgain = input()
    if playAgain == "no":
      # spelling mistake on line 72, planing should be playing
        print("Thanks for planing")