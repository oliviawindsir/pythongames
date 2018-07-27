#----------------------------------------------------------------------------
#Play a game of bingo
#Rule :
#       1. Fill in number 1-25 in a 5x5 box of your preference
#       2. Pick a number to start. Both computer and you cross out the number
#          that has been called.
#       3. Computer calls a number and both you and computer cross out the
#          called number.
#       4. Whenever a straight/diagonal 5 boxes has been crossed, form an
#          alphabet from 'B-I-N-G-O'
#       5. The first to form complete 5 letters 'B-I-N-G-O' wins.
#-----------------------------------------------------------------------------

#Constants
MAX_ROW = 5
MAX_COL = 5

def init_boxes():

    #player_grid=[[0] * MAX_COL for row in range(MAX_ROW)]
    player_box = []

    for col in range(MAX_COL):
        print('Enter any 5 values from 1-25 for row')
        player_box.append([int(j) for j in input().split()])
    
        print('You filled in : ')
        for row in player_box:
            for elem in row:
                if elem > 25:
                    print('ERROR: Value cannot be more than 25')
                    return -1;
            print(' '.join([str(elem) for elem in row]))

#main program
init_boxes()
            
