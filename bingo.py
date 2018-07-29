#----------------------------------------------------------------------------
#Play a game of bingo
#Rule :
#       1. Start a game - randomly generate Player Grid and Comp Grid 
#       2. Pick a number to start. Both computer and you cross out the number
#          that has been called.
#       3. Computer calls a number and both you and computer cross out the
#          called number.
#       4. Whenever a straight/diagonal 5 boxes has been crossed, form an
#          alphabet from 'B-I-N-G-O'
#       5. The first to form complete 5 letters 'B-I-N-G-O' wins.
#-----------------------------------------------------------------------------

import random
import tkinter
from tkinter import *
from random import randint
from random import shuffle

#Constants
BINGO_GRID = 5
BINGO_START_NUM = 1
BINGO_END_NUM = BINGO_GRID * BINGO_GRID


#Create new game
def createNewGame():
    num_list = list(range(BINGO_START_NUM,BINGO_END_NUM+1))

    shuffle(num_list)
    player_grid = to_matrix(num_list,BINGO_GRID)
    print(player_grid)

    shuffle(num_list)
    comp_grid = to_matrix(num_list,BINGO_GRID)
    print(comp_grid)

#Convert a list to 2d array
def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

#MAIN program
createNewGame()
            
