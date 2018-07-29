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
CHECKED_GRID = 1
UNCHECKED_GRID = 0


#Create new game
def createGrid():
    num_list = list(range(BINGO_START_NUM,BINGO_END_NUM+1))

    shuffle(num_list)
    grid = to_matrix(num_list,BINGO_GRID)
    print(grid)

    return grid

#Convert a list to 2d array
def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]


#MAIN program
called_list = []
mask_bingo_grid = [[0] * BINGO_GRID for n in range(BINGO_GRID)]

player_grid = createGrid()
comp_grid = createGrid()

isBingo = True

#Start Game
while isBingo:
    num_picked = int(input('Pick a number from 1-25: \n'))

    if num_picked in called_list:
        print('Number has been called before. Choose another one')

    if num_picked > 25 and num_picked <= 0:
        print('Invalid entry!')
    else:
        #checks where is the number coordinate
        elem = [elem for elem in player_grid if int(num_picked) in elem][0]
        print(elem)
        print('The index is (%d, %d)' %(player_grid.index(elem), elem.index(num_picked)))

        mask_bingo_grid[player_grid.index(elem)][elem.index(num_picked)] = CHECKED_GRID
        print(mask_bingo_grid)
        called_list.append(num_picked)
        print(called_list)

    





            
