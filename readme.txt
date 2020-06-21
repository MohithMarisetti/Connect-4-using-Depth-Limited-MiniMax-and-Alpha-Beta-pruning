Depth Limited MiniMax with Alpha Beta pruning
Author Name: Mohith Marisetti	
Language Used: Python 2.x
Additional Code Files: None 

Code Structure:
Implemented the functionality in oneMoveGame(currentGame,depth) and interactiveGame(currentGame,depth, firstPlayer) functions
All the minimax logic is kept in the MaxConnect4Game.py file at the bottom. New functions implemented are 
1)utilityValOfNTNode(gameState): This function calculates the utility value of a given game state.
2)maxValue(gameState,alpha,beta) : This function is used to calculate the min value and use given alpha, beta values to prune any unneccsary nodes.
3)minValue(gameState,alpha,beta) : This function is used to calculate the min value and use given alpha, beta values to prune any unneccsary nodes.
4)minimax(gameState,depth) : This function is used to get the column for which the winning chance is max as calculated by the heuristic.


How to execute the code:
To specifically run on python 2 if your system has both python2 and python 3 is as follows:
For interactive mode:	$py -2 maxconnect4.py interactive input1.txt human-next 5
For one-move mode: 	$py -2 maxconnect4.py one-move input1.txt output1.txt 5

or else if only python2 is installed.,
For interactive mode: 	$python maxconnect4.py interactive input1.txt human-next 5
For one-move mode:	$python maxconnect4.py one-move input1.txt output1.txt 5   (For the first run) 
			For the next set of operations use $python maxconnect4.py one-move output1.txt output1.txt 5

