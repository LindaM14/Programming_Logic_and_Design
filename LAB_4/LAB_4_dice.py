"""
Generate random numbers for the user
Emulate rolling a dice, until user wants to quit
Uses f-strings also known as format strings
"""

import random # imports python codes

want_to_quit = '' # following line 19

while not want_to_quit: # create a loop, rolling 2 dice at the same time
    dice_value_1 = random.randint(1, 6) # dice rolls from 1-6
    dice_value_2 = random.randint(1,6) # dice rolls from 1-6
    print(f'You rolled a {dice_value_1} and {dice_value_2}')

    if dice_value_1 == dice_value_2: # if rolling a double print user that they can roll again
        print(f'You rolled a double! roll again ')

    want_to_quit = input('Press enter to roll again, any other key to quit ') # to end the program anything else besides hitting enter "exit" for example