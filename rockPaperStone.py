#Rock Paper Stone

import string
import random
from random import randint

#internal functions
def convert_caseInsensitive(str):
    new_str = str.lower()
    return new_str

#main loop starts
loopagain = True

while loopagain:
    player = input('Rock(r), Paper(p) or Stone(s)?')
    player = convert_caseInsensitive(player)
    
    str_choices = 'rps'
    comp = random.choice(str_choices)
    convert_caseInsensitive(comp)

    print('You : ' + player + ' vs ' + 'Comp : ' + comp)

#check condition of winning/losing
    if player == comp:
        print ('DRAW')
    elif(   (player == 'r' and comp == 'p') or
            (player == 'p' and comp == 's') or
            (player == 's' and comp == 'r')):
        print ('You lose')
    elif(   (player == 'p' and comp == 'r') or
            (player == 's' and comp == 'p') or
            (player == 'r' and comp == 's')):
        print ('You win')
    else:
        print ('What?!')

#check for replay
    try_again = input('Try again? (y/n)')
    if try_again == 'n':
        loopagain = False
    elif try_again == 'y':
        loopagain == True
    else:
        print('Invalid entry')

#exit message
print('Thanks for playing!')



