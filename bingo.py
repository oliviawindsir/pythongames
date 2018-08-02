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

'''Constants for a 5x5 grid'''
GRID_SIZE = 5
BINGO_START_NUM = 1
BINGO_END_NUM = GRID_SIZE * GRID_SIZE
CHECKED_GRID = 1
UNCHECKED_GRID = 0

class Grid:
    '''Initialize grid properties'''
    def __init__(self):
        self.gridSize = GRID_SIZE
        self.minVal = BINGO_START_NUM
        self.maxVal = BINGO_END_NUM
        print('Initialized grid properties')

    '''Create grid with randomly allocated num within range'''
    def createStatusBoard(self):
        grid = []
        grid = [[0] * GRID_SIZE for n in range(GRID_SIZE)]
        print('Created status grid of size ' + str(self.gridSize) + 'X' + str(self.gridSize))
        return grid

    def createPlayBoard(self):
        num_list = list(range(self.minVal,self.maxVal+1))
        shuffle(num_list)
        grid = Utilities.to_matrix(num_list,GRID_SIZE)
        print('Created play grid of size ' + str(self.gridSize) + 'X' + str(self.gridSize))
        return grid

class Players(Grid):    
    '''Initialize player properties'''
    def createPlayer(self):
        self.gridBoard = Grid.createPlayBoard(self)
        self.statusBoard = Grid.createStatusBoard(self)
        self.status = []
        print('Player initialized with a grid and status board')
        return True

    def checkPlayBoard(self, number):
        '''checks where is the number coordinate'''
        elem = [elem for elem in self.gridBoard if int(number) in elem][0]
        print('The index is (%d, %d)' %(self.gridBoard.index(elem), elem.index(number)))
        self.statusBoard[self.gridBoard.index(elem)][elem.index(number)] = CHECKED_GRID
        print('Successfully crossed out ' + str(number) + '!')
        return True

    def checkStatusBoard(self):
        '''checks if horizontal pattern has been fulfilled'''
        crossedOut_horizontal = [0] * GRID_SIZE
        for row in self.statusBoard:
            if row.count(0) == 0:
                crossedOut_horizontal[row] = 1

##            if crossedOut_horizontal[row] == 1:
##                bingoCount+=1
##                crossedOut_horizontal[row] = 2
##            else:
##                #remain unchanged

##        '''checks if vertical pattern has been fulfilled'''
##        crossedOut_vertical = [0] * GRID_SIZE
##        for row in GRID_SIZE:
##            list_ver = []
##            for col in GRID_SIZE:
##                list_ver.append(vert[col][row])
##
##            if list_ver.count(0) == 0:
##                crossedOut_hor[row] = 1
##
##            if crossedOut_hor[row] = 1
##                bingoCount+=1
##                crossedOut_hor[row] = 2
##            else:
##                #remain unchanged

class Utilities:
    '''Convert a list to 2d array'''
    def to_matrix(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]
        
     


#MAIN program
uncalledNum = list(range(BINGO_START_NUM, BINGO_END_NUM+1))

#Create player
player = Players()
player.createPlayer()

#Create computer opponent
comp = Players()
comp.createPlayer()

#Start the game to call numbers
isGameOn = True

while isGameOn:
    
    isNotValidRound = True
    #Call a number and checks for validity
    while isNotValidRound:
        numCalled = int(input('Player call a number ranging between 1-25\n'))
        
        if numCalled > 0 and numCalled < 25 and numCalled in uncalledNum:
            player.checkPlayBoard(numCalled)
            comp.checkPlayBoard(numCalled)
            uncalledNum.remove(numCalled)
            isNotValidRound = True
            break;
        else:
            print('Invalid number. Please re-enter.')

    #Check if you filled any pattern
    player.checkStatusBoard()
    comp.checkStatusBoard()

    #Computer calls a number
    print('Comp call a number ranging between 1-25')
    comp.checkPlayBoard(4)
    player.checkPlayBoard(4)

    #Check if fulfill any pattern
    player.checkStatusBoard()
    comp.checkStatusBoard()





            
