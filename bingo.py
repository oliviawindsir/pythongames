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
##        print('Initialized grid properties')

    '''Create grid with randomly allocated num within range'''
    def createStatusBoard(self):
        grid = []
        grid = [[0] * GRID_SIZE for n in range(GRID_SIZE)]
##        print('Created status grid of size ' + str(self.gridSize) + 'X' + str(self.gridSize))
        return grid

    def createPlayBoard(self):
        num_list = list(range(self.minVal,self.maxVal+1))
        shuffle(num_list)
        grid = Utilities.to_matrix(num_list,GRID_SIZE)
####        print('Created play grid of size ' + str(self.gridSize) + 'X' + str(self.gridSize))
        return grid

class Players(Grid):    
    '''Initialize player properties'''
    def createPlayer(self, name):
        self.name = name
        self.playBoard = Grid.createPlayBoard(self)
        self.statusBoard = Grid.createStatusBoard(self)
        self.countHorizontalMatch = 0
        self.countVerticalMatch = 0
        self.countDiagonalMatch = 0
        print('Player initialized with a grid and status board')
        return True

    def getName(self):
        playerName = str(self.name)
        return playerName

    def displayPlayBoard(self):
        print(self.playBoard)

    def displayStatusBoard(self):
        print(self.statusBoard)

    def checkPlayBoard(self, number):
        '''checks where is the number coordinate'''
        elem = [elem for elem in self.playBoard if int(number) in elem][0]
        self.statusBoard[self.playBoard.index(elem)][elem.index(number)] = CHECKED_GRID
        print('Successfully crossed out ' + str(number) + ' on ' + self.name + ' board!')
        return True

    def checkStatusBoard(self):
        
        totalMatchingPattern = 0
        
        '''checks if horizontal pattern has been fulfilled'''
        matchingPattern = 0
        for rowList in self.statusBoard:
            if rowList.count(0) == 0:
                matchingPattern += 1

        if matchingPattern > self.countHorizontalMatch:
            self.countHorizontalMatch = matchingPattern
##            print('Horizontal count = ' + str(self.countHorizontalMatch))

        '''checks if vertical pattern has been fulfilled'''
        matchingPattern = 0
        crossedOut_vertical = [0] * GRID_SIZE
        for row in range(GRID_SIZE):
            list_ver = []
            for col in range(GRID_SIZE):
                list_ver.append(self.statusBoard[col][row])

            if list_ver.count(0) == 0:
                matchingPattern += 1

            if matchingPattern > self.countVerticalMatch:
                self.countVerticalMatch = matchingPattern
##                print('Vertical count = ' + str(self.countVerticalMatch))

        '''checks if diagonal pattern has been fulfilled'''
        crossedOut_diagonal = [0] * GRID_SIZE
        matchingPattern = 0
        list_diagLeft = []
        list_diagRight = []
        for row in range(GRID_SIZE):
            list_diagLeft.append(self.statusBoard[row][row])
            list_diagRight.append(self.statusBoard[row][(GRID_SIZE-1)-row])

        if list_diagLeft.count(0) == 0:
            matchingPattern += 1

        if list_diagRight.count(0) == 0:
            matchingPattern += 1
            

        if matchingPattern > self.countDiagonalMatch:
            self.countDiagonalMatch = matchingPattern
##            print('Diagonal count = ' + str(self.countDiagonalMatch))
        
        totalMatchingPattern = self.countHorizontalMatch + self.countVerticalMatch + self.countDiagonalMatch
        print(self.name + ' Number of matching pattern : ' + str(totalMatchingPattern))
        if totalMatchingPattern >= 5:
            print(self.name + ' calls Bingo!')
            return False
        return True

class Utilities:
    '''Convert a list to 2d array'''
    def to_matrix(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]
        
     


#MAIN program
uncalledNum = list(range(BINGO_START_NUM, BINGO_END_NUM+1))

#Create player
player = Players()
player.createPlayer("WS")
player.displayPlayBoard()

#Create computer opponent
comp = Players()
comp.createPlayer("COMP")

#Start the game to call numbers
# 1. Randomly select who to start first. Odd num - Player, Even num - Comp
seed = random.choice(range(8))

# 2. Turn on the game switch
isGameOn = True
while isGameOn:

    if seed%2 != 0:
        isNotValidRound = True
        #Call a number and checks for validity
        while isNotValidRound:
            numCalled = int(input('\nPlayer choose a number between 1-25\n'))
            print('Player called : ' + str(numCalled))
            if numCalled > 0 and numCalled <=25  and numCalled in uncalledNum:
                player.checkPlayBoard(numCalled)
                comp.checkPlayBoard(numCalled)
                uncalledNum.remove(numCalled)
                isNotValidRound = True
                break;
            else:
                print('\nInvalid number. Please re-enter.')

        #Check if you filled any pattern
        isGameOn = player.checkStatusBoard() and comp.checkStatusBoard()
        print('\nPlayer status board: ')
        player.displayStatusBoard()
        print('\nPlayer play board: ')
        player.displayPlayBoard()
        seed += 1

    else:
        #Computer calls a number
        print('\nCOMP\'s turn : ')
        numCalled = random.choice(uncalledNum)
        print('COMP called : ' + str(numCalled))
        comp.checkPlayBoard(numCalled)
        player.checkPlayBoard(numCalled)
        uncalledNum.remove(numCalled)

        #Check if you filled any pattern
        isGameOn = player.checkStatusBoard() and comp.checkStatusBoard()
        print('\nPlayer status board: ')
        player.displayStatusBoard()
        seed += 1

print('Game ended')





            
