#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
from MaxConnect4Game import *

def oneMoveGame(currentGame,depth):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)

    #currentGame.aiPlay() # Make a move (only random is implemented)
    minimax(currentGame,depth)


    print 'Game state after move:'
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame,depth, firstPlayer):
    # Fill me in
    # sys.exit('Interactive mode is currently not implemented')
    if currentGame.pieceCount == 42:    # Is the board full already?
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)

    if firstPlayer == "computer-next":
        minimax(currentGame,depth)


        print 'Game state after move:'
        #currentGame.printGameBoard()
        print ' -----------------'
        for i in range(6):
            print ' |',
            for j in range(7):
                print('%d' % currentGame.gameBoard[i][j]),
            print '| '
        print ' -----------------'


        currentGame.countScore()
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    
    
    #while pieces there to play, play the game with the Human
    try:
        while(currentGame.pieceCount<42):
            try:
                userColumn = input("Select a column to insert:")
                userColumn-=1
            except:
                print("Please enter a number")
           
            try:
                if not currentGame.playPiece(userColumn):
                    print('Please select a valid column and try again!')
                    continue
            except:
                print('Please select a valid column and try again!')
                continue
            print('Game state after move')
            



            print ' -----------------'
            for i in range(6):
                print ' |',
                for j in range(7):
                    print('%d' % currentGame.gameBoard[i][j]),
                print '| '
            print ' -----------------'

            




            currentGame.countScore()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            



            if currentGame.currentTurn==1:
                currentGame.currentTurn = 2
            else:
                currentGame.currentTurn = 1

            minimax(currentGame,depth)
            
            
            print ' -----------------'
            for i in range(6):
                print ' |',
                for j in range(7):
                    print('%d' % currentGame.gameBoard[i][j]),
                print '| '
            print ' -----------------'








            currentGame.countScore()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    except:
        currentGame.printGameBoardToFile
    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()



def main(argv):
    # Make sure we have enough command-line arguments
    start = time.time()
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]
    depth = argv[4]


    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        
        try:
            if argv[3]=="computer-next":
                currentGame.gameFile = open("computer.txt", 'w')
            else:
                currentGame.gameFile = open("human.txt", 'w')
        except:
            sys.exit('Error opening output file.')
        interactiveGame(currentGame,depth,argv[3]) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame,depth) # Be sure to pass any other arguments from the command line you might need.
        end = time.time()
        #print("Execution time = %s",(end-start))

if __name__ == '__main__':
    main(sys.argv)



