"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

from random import randint
def computer_guess_number():
    # initial low and high bounds
    low = 1
    high = 100
    n = randint(low,high) # guess number between 1 and 100
    print(f'Here\'s my first guess ! - {n}\n')
    while True:
        # get user feedback - is the number too high, too low, or the correct guess
        choice = input('Pick an option:\n\n too low (or type L)/\ntoo high (or type H)/\ncorrect (or type C) !\n')
        if choice == 'too low' or choice == 'L': # if guess was too low
            # reset the lower bound 
            low = n+1
            # guess again between low bound and high bound
            n = randint(low,high)
            print(f'a higher guess: {n}')
            continue
        elif choice == 'too high' or choice == 'H': # if guess was too high
            # reset the high bound 
            high = n-1
            # guess again within the current low and high limits
            n = randint(low, high)
            print(f'a lower guess: {n}')
            continue
        elif choice == 'correct' or choice == 'C': # if guess was correct
            print(f'I got it! The number was {n}')
            return False
        else: # if user input didn't match the choices
            print('Please choose one of the three options')
            continue
        

computer_guess_number()
