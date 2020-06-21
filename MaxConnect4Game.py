#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

from copy import *
import random
import sys
import time
import math

depth = 2
player1 = 1
player2 = 2

class maxConnect4Game:
    def __init__(self):
        self.gameBoard = [[0 for i in range(7)] for j in range(6)]
        self.currentTurn = 1
        self.player1Score = 0
        self.player2Score = 0
        self.pieceCount = 0
        self.gameFile = None
        random.seed()

    # Count the number of pieces already played
    def checkPieceCount(self):
        self.pieceCount = sum(1 for row in self.gameBoard for piece in row if piece)

    # Output current game status to console
    def printGameBoard(self):
        print ' -----------------'
        for i in range(6):
            print ' |',
            for j in range(7):
                print('%d' % self.gameBoard[i][j]),
            print '| '
        print ' -----------------'

    # Output current game status to file
    def printGameBoardToFile(self):
        for row in self.gameBoard:
            self.gameFile.write(''.join(str(col) for col in row) + '\r\n')
        self.gameFile.write('%s\r\n' % str(self.currentTurn))

    # Place the current player's piece in the requested column
    def playPiece(self, column):
        if not self.gameBoard[0][column]:
            for i in range(5, -1, -1):
                if not self.gameBoard[i][column]:
                    self.gameBoard[i][column] = self.currentTurn
                    self.pieceCount += 1
                    return 1

    

    # # The AI section. Currently plays randomly.
    # def aiPlay(self):
    #     if self.pieceCount == 0:
    #         randColumn = random.randrange(0,7)
    #         result = self.playPiece(randColumn)
    #         if not result:
    #             self.aiPlay()
    #         else:
    #             print('\n\nmove %d: Player %d, column %d\n' % (self.pieceCount, self.currentTurn, randColumn+1))
    #             if self.currentTurn == 1:
    #                 self.currentTurn = 2
    #             elif self.currentTurn == 2:
    #                 self.currentTurn = 1
    #     else:
    #         if(self.currentTurn==1): #MAX PLAYER
    #             #MAX ALGO CALL
    #             d = 5
    #             for i in range(1,8):
    #                 maxGame[i] = self.gameBoard
    #                 maxGame[i].playPiece(i)
    #                 for j in range(d):
                        
    #         else: #MIN PLAYER
    #             #MIN ALGO CALL




    # Calculate the number of 4-in-a-row each player has
    def countScore(self):
        self.player1Score = 0;
        self.player2Score = 0;

        # Check horizontally
        for row in self.gameBoard:
            # Check player 1
            if row[0:4] == [1]*4:
                self.player1Score += 1
            if row[1:5] == [1]*4:
                self.player1Score += 1
            if row[2:6] == [1]*4:
                self.player1Score += 1
            if row[3:7] == [1]*4:
                self.player1Score += 1
            # Check player 2
            if row[0:4] == [2]*4:
                self.player2Score += 1
            if row[1:5] == [2]*4:
                self.player2Score += 1
            if row[2:6] == [2]*4:
                self.player2Score += 1
            if row[3:7] == [2]*4:
                self.player2Score += 1

        # Check vertically
        for j in range(7):
            # Check player 1
            if (self.gameBoard[0][j] == 1 and self.gameBoard[1][j] == 1 and
                   self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][j] == 1 and self.gameBoard[2][j] == 1 and
                   self.gameBoard[3][j] == 1 and self.gameBoard[4][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1 and
                   self.gameBoard[4][j] == 1 and self.gameBoard[5][j] == 1):
                self.player1Score += 1
            # Check player 2
            if (self.gameBoard[0][j] == 2 and self.gameBoard[1][j] == 2 and
                   self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][j] == 2 and self.gameBoard[2][j] == 2 and
                   self.gameBoard[3][j] == 2 and self.gameBoard[4][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2 and
                   self.gameBoard[4][j] == 2 and self.gameBoard[5][j] == 2):
                self.player2Score += 1

        # Check diagonally

        # Check player 1
        if (self.gameBoard[2][0] == 1 and self.gameBoard[3][1] == 1 and
               self.gameBoard[4][2] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][0] == 1 and self.gameBoard[2][1] == 1 and
               self.gameBoard[3][2] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][1] == 1 and self.gameBoard[3][2] == 1 and
               self.gameBoard[4][3] == 1 and self.gameBoard[5][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][0] == 1 and self.gameBoard[1][1] == 1 and
               self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][1] == 1 and self.gameBoard[2][2] == 1 and
               self.gameBoard[3][3] == 1 and self.gameBoard[4][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1 and
               self.gameBoard[4][4] == 1 and self.gameBoard[5][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][1] == 1 and self.gameBoard[1][2] == 1 and
               self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][2] == 1 and self.gameBoard[2][3] == 1 and
               self.gameBoard[3][4] == 1 and self.gameBoard[4][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1 and
               self.gameBoard[4][5] == 1 and self.gameBoard[5][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][2] == 1 and self.gameBoard[1][3] == 1 and
               self.gameBoard[2][4] == 1 and self.gameBoard[3][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][4] == 1 and
               self.gameBoard[3][5] == 1 and self.gameBoard[4][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][4] == 1 and
               self.gameBoard[2][5] == 1 and self.gameBoard[3][6] == 1):
            self.player1Score += 1

        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][2] == 1 and
               self.gameBoard[2][1] == 1 and self.gameBoard[3][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][4] == 1 and self.gameBoard[1][3] == 1 and
               self.gameBoard[2][2] == 1 and self.gameBoard[3][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][2] == 1 and
               self.gameBoard[3][1] == 1 and self.gameBoard[4][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][5] == 1 and self.gameBoard[1][4] == 1 and
               self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][4] == 1 and self.gameBoard[2][3] == 1 and
               self.gameBoard[3][2] == 1 and self.gameBoard[4][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1 and
               self.gameBoard[4][1] == 1 and self.gameBoard[5][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][6] == 1 and self.gameBoard[1][5] == 1 and
               self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][5] == 1 and self.gameBoard[2][4] == 1 and
               self.gameBoard[3][3] == 1 and self.gameBoard[4][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1 and
               self.gameBoard[4][2] == 1 and self.gameBoard[5][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][6] == 1 and self.gameBoard[2][5] == 1 and
               self.gameBoard[3][4] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][5] == 1 and self.gameBoard[3][4] == 1 and
               self.gameBoard[4][3] == 1 and self.gameBoard[5][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][6] == 1 and self.gameBoard[3][5] == 1 and
               self.gameBoard[4][4] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1

        # Check player 2
        if (self.gameBoard[2][0] == 2 and self.gameBoard[3][1] == 2 and
               self.gameBoard[4][2] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][0] == 2 and self.gameBoard[2][1] == 2 and
               self.gameBoard[3][2] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][1] == 2 and self.gameBoard[3][2] == 2 and
               self.gameBoard[4][3] == 2 and self.gameBoard[5][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][0] == 2 and self.gameBoard[1][1] == 2 and
               self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][1] == 2 and self.gameBoard[2][2] == 2 and
               self.gameBoard[3][3] == 2 and self.gameBoard[4][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2 and
               self.gameBoard[4][4] == 2 and self.gameBoard[5][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][1] == 2 and self.gameBoard[1][2] == 2 and
               self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][2] == 2 and self.gameBoard[2][3] == 2 and
               self.gameBoard[3][4] == 2 and self.gameBoard[4][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2 and
               self.gameBoard[4][5] == 2 and self.gameBoard[5][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][2] == 2 and self.gameBoard[1][3] == 2 and
               self.gameBoard[2][4] == 2 and self.gameBoard[3][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][4] == 2 and
               self.gameBoard[3][5] == 2 and self.gameBoard[4][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][4] == 2 and
               self.gameBoard[2][5] == 2 and self.gameBoard[3][6] == 2):
            self.player2Score += 1

        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][2] == 2 and
               self.gameBoard[2][1] == 2 and self.gameBoard[3][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][4] == 2 and self.gameBoard[1][3] == 2 and
               self.gameBoard[2][2] == 2 and self.gameBoard[3][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][2] == 2 and
               self.gameBoard[3][1] == 2 and self.gameBoard[4][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][5] == 2 and self.gameBoard[1][4] == 2 and
               self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][4] == 2 and self.gameBoard[2][3] == 2 and
               self.gameBoard[3][2] == 2 and self.gameBoard[4][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2 and
               self.gameBoard[4][1] == 2 and self.gameBoard[5][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][6] == 2 and self.gameBoard[1][5] == 2 and
               self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][5] == 2 and self.gameBoard[2][4] == 2 and
               self.gameBoard[3][3] == 2 and self.gameBoard[4][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2 and
               self.gameBoard[4][2] == 2 and self.gameBoard[5][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][6] == 2 and self.gameBoard[2][5] == 2 and
               self.gameBoard[3][4] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][5] == 2 and self.gameBoard[3][4] == 2 and
               self.gameBoard[4][3] == 2 and self.gameBoard[5][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][6] == 2 and self.gameBoard[3][5] == 2 and
               self.gameBoard[4][4] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1


"""
This function is used to get the column for which the winning 
chance is max as calculated by the heuristic
"""
def minimax(gameState,d):
    
    global player1
    global player2
    global depth 
    alpha = -9999   #We initialize the alpha & beta with the worst values
    beta = 9999

    depth = int(d)   #d is the provided depth given in cmd line
    
    #We call the maxValue algorithm to calculate the max value for the given state
    dict = maxValue(gameState,alpha,beta)  

    player1 = gameState.currentTurn  #Set the player 1 and player2 globally
    if player1 == 1:
        player2 = 2
    elif player1 == 2:
        player2 = 1

    #Index of the column with the max value possible
    column = dict["index"]
    gameState.playPiece(column)
    
    #We change the turn to save the next players turn in the file
    if gameState.currentTurn == 1:
        gameState.currentTurn = 2
    elif gameState.currentTurn == 2:
        gameState.currentTurn = 1


"""
This function is used to calculate the min value and use given
alpha, beta values to prune any unneccsary nodes
"""
def minValue(gameState,alpha,beta): 
    minimumIndex = -1
    minimumValue = 99999
    availableColumnsList = []
    global depth  
    
    #Make a copy of the game state
    newGameState2 = deepcopy(gameState)

    if depth>0:
        depth = depth-1  #Decrese the depth value
        

        #Find out the available columns
        for eachrow in newGameState2.gameBoard:
            if eachrow[0]==0 and (0 not in availableColumnsList):
                availableColumnsList.append(0)
            if eachrow[1]==0 and (1 not in availableColumnsList):
                availableColumnsList.append(1)
            if eachrow[2]==0 and (2 not in availableColumnsList):
                availableColumnsList.append(2)
            if eachrow[3]==0 and (3 not in availableColumnsList):
                availableColumnsList.append(3)
            if eachrow[4]==0 and (4 not in availableColumnsList):
                availableColumnsList.append(4)
            if eachrow[5]==0 and (5 not in availableColumnsList):
                availableColumnsList.append(5)
            if eachrow[6]==0 and (6 not in availableColumnsList):
                availableColumnsList.append(6)
            
        #process the available columns  
        for i in availableColumnsList:
            newGameState = deepcopy(newGameState2) #Make a copy
            
            #play a turn in an available column
            newGameState.playPiece(i)
            if depth != 0:   #If depth not 0 go to next level
                
                # Turn the currentTurn to other players turn so as to perform 
                # min calculation as second player
                if newGameState.currentTurn == 1:
                    newGameState.currentTurn = 2
                elif newGameState.currentTurn == 2:
                    newGameState.currentTurn = 1
            
                # Call the maxValue function and iterate till we hit the resource depth limit
                tempDict = maxValue(newGameState,alpha,beta)
                tempVal = tempDict["value"]

                # If value got is even less than the current Min node's value has 
                # then swap the values
                if tempVal<minimumValue:
                    minimumValue = tempVal
                    minimumIndex = i
                
                # Basic Alpha Beta pruning Logic at Min node
                if tempVal<beta:
                    beta=tempVal
                if tempVal<=alpha:
                    break

                # We swap the currentTurn back to the same Node
                if newGameState.currentTurn == 1:
                    newGameState.currentTurn = 2
                elif newGameState.currentTurn == 2:
                    newGameState.currentTurn = 1
            
            else:
                # If depth limit reached then we calculate the utility values for each
                # of the game state 
                utilityValue = utilityValOfNTNode(newGameState)
                #If the utility value is lesser than the prev minimum val then we swap it
                if (utilityValue < minimumValue):
                    minimumValue = utilityValue
                    minimumIndex = i
        

        #We create a dictionary to send the min index and min value we found 
        d = dict()
        d["index"] = minimumIndex
        d["value"] = minimumValue
        
        depth = depth+1  #Increment the depth limit by 1 to allow further processing of new available columns
        return d  #Return the dictionary object


"""
This function is used to calculate the min value and use given
alpha, beta values to prune any unneccsary nodes
"""
def maxValue(gameState,alpha,beta):
    minmaxValList = []
    availableColumnsList = []
    maxValue = -9999
    maxIndex = -1
    global depth
    if depth>0:
        #Decrese the depth value
        depth = depth-1
        #Make a Copy of the game State
        newGameState2 = deepcopy(gameState)

        #Find out the available columns
        for eachrow in newGameState2.gameBoard:
            if eachrow[0]==0 and (0 not in availableColumnsList):
                availableColumnsList.append(0)
            if eachrow[1]==0 and (1 not in availableColumnsList):
                availableColumnsList.append(1)
            if eachrow[2]==0 and (2 not in availableColumnsList):
                availableColumnsList.append(2)
            if eachrow[3]==0 and (3 not in availableColumnsList):
                availableColumnsList.append(3)
            if eachrow[4]==0 and (4 not in availableColumnsList):
                availableColumnsList.append(4)
            if eachrow[5]==0 and (5 not in availableColumnsList):
                availableColumnsList.append(5)
            if eachrow[6]==0 and (6 not in availableColumnsList):
                availableColumnsList.append(6)
            
        #process the available columns
        for i in availableColumnsList:
            newGameState = deepcopy(newGameState2)  #Make a copy 

            #play a turn in an available column
            newGameState.playPiece(i)
            
            if depth!=0: #If depth not 0 go to next level
                
                # Turn the currentTurn to other players turn so as to perform 
                # min calculation as second player
                if newGameState.currentTurn == 1:
                    newGameState.currentTurn = 2
                elif newGameState.currentTurn == 2:
                    newGameState.currentTurn = 1
            
                # Call the minValue function and iterate till we hit the resource depth limit
                tempDict = minValue(newGameState,alpha,beta)
                tempVal = tempDict["value"]
                
                # If value got is even more than the current Max node's value has 
                # then swap the values
                if tempVal>maxValue:
                    maxValue = tempVal
                    maxIndex = i

                # Basic Alpha Beta pruning Logic at Max node
                if tempVal>alpha:
                    alpha = tempVal
                if tempVal>=beta:
                    
                    break
                
            # We swap the currentTurn back to the same Node
                if newGameState.currentTurn == 1:
                    newGameState.currentTurn = 2
                elif newGameState.currentTurn == 2:
                    newGameState.currentTurn = 1
            
            
            else: #We calculate the utility value for that state
                utilityValue = utilityValOfNTNode(newGameState)
                #If the utility value is greater than the prev maximum val then we swap it
                if (utilityValue > maxValue):
                    maxValue = utilityValue
                    maxIndex = i

            # We get back the value from the minValue function and then change turn back to 
            # Max Player 

        #We create a dictionary to send the min index and min value we found 
        d = dict()
        d["index"] = maxIndex
        d["value"] = maxValue
        
        depth = depth+1 #Increment the depth limit by 1 to allow further processing of new available columns
        return d           #Return the dictionary object
    


"""
This function calculates the utility value of a given game state
"""
def utilityValOfNTNode(gameState):

    gameState.countScore
    utility = 0
    player = []  #We initialize the player as list
    altplayer = []  #we initialize the alternate player as list
    global player1
    if player1 == 1:
        player = [1]   #set the player to 1 and altplayer to 2 for further calculations
        altplayer = [2]
    else:
        player = [2]
        altplayer = [1]
    
    for row in gameState.gameBoard:
        temp = 0
        for v in row:
            if (v == 0):
                temp+=1
        if(temp==7):
            continue
        else:    
            
            #Number of player's 2 in a row
            if row[0:2] == player*2 and row[2:4]==[0]*2:
                utility +=80
            if row[1:3] == player*2 and row[3:5]==[0]*2:
                utility +=80
            if (row[2:4] == player*2 and row[4:6]==[0]*2) or (row[2:4] == player*2 and row[0:2]==[0]*2):
                utility +=100
            if (row[3:5] == player*2 and row[5:7]==[0]*2) or (row[3:5] == player*2 and row[1:3]==[0]*2):
                utility +=130
            if row[4:6] == player*2 and row[2:4]==[0]*2:
                utility +=80
            if row[5:7] == player*2 and row[3:5]==[0]*2:
                utility +=80
            #Number of alternate player's 2 in a row
            if row[0:2] == altplayer*2 and row[2:4]==[0]*2:
                utility -=80
            if row[1:3] == altplayer*2 and row[3:5]==[0]*2:
                utility -=80
            if (row[2:4] == altplayer*2 and row[4:6]==[0]*2) or (row[2:4] == altplayer*2 and row[0:2]==[0]*2):
                utility -=100
            if (row[3:5] == altplayer*2 and row[5:7]==[0]*2) or (row[3:5] == altplayer*2 and row[1:3]==[0]*2):
                utility -=130
            if row[4:6] == altplayer*2 and row[2:4]==[0]*2:
                utility -=80
            if row[5:7] == altplayer*2 and row[3:5]==[0]*2:
                utility -=80
            
            



            # Number of player's 3 in a row
            if row[0:3] == player*3 and row[4]==0:
                utility +=100
            if ((row[1:4] == player*3 and row[4]==0) or (row[1:4] == player*3 and row[0]==0)):
                utility +=100
            if (row[2:5] == player*3 and row[5]==0) or (row[2:5] == player*3 and row[1]==0):
                utility +=100
            if (row[3:6] == player*3 and row[6]==0) or (row[3:6] == player*3 and row[2]==0):
                utility +=100
            if (row[4:7] == player*3 and row[3]==0):
                utility +=100

            #Number of alternate player's 3 in a row
            if row[0:3] == altplayer*3 and row[4]==0:
                utility -=50
            if (row[1:4] == altplayer*3 and row[4]==0) or (row[1:4] == altplayer*3 and row[0]==0):
                utility -=50
            if (row[2:5] == altplayer*3 and row[5]==0) or (row[2:5] == altplayer*3 and row[1]==0):
                utility -=50
            if (row[3:6] == altplayer*3 and row[6]==0) or (row[3:6] == altplayer*3 and row[2]==0):
                utility -=50
            if (row[4:7] == altplayer*3 and row[3]==0):
                utility -=50
        

            # If current player keeps his number in the 3rd 
            # index(4th column) then his chances of winning are 
            # very high(So, utility of 200)
            if (row[3]==player[0]) : #player = [1] . So, player[0] means 1
                utility+=200
            
            # If other player keeps his number in the 3rd 
            # index(4th column) then his chances of winning are 
            # very high(So, utility of -150)
            
            if row[3]==altplayer[0]:
                utility-=150
            
            if (row[3]==player[0] and row[4]==0) or (row[3]==player[0] and row[2]==0):
                utility+=150
            
    
    

    # IF current player has a state with more score 
    # he has a greater utility value in that state
    # (so 300 utility value)
    if gameState.currentTurn == player1: 
        value =  gameState.player1Score - gameState.player2Score
        if value>0:
            utility+=300
        else:
            utility -= 300
    
    # IF other player has a state with more score 
    # player1 has a lesser utility value in that state
    # (so -300 utility value)
    else: 
        value = gameState.player2Score - gameState.player1Score
        if value>0:
            utility+=300
        else:
            utility -= 300

    
    return utility

