"""
This python file will have functions that will be used to create the game in Main.py

-setting up the dimensions of the board
-setting up the bombs of the board
-setting up the number of bombs surrounding
-setting up blank empty tiles

Actions/Commands of the game will be located in another file


"""
from Tile import Tile

#========================================================================================================================
#function to create the gameboard
#for now we will hardcode a specific size, later we will ask it as userinput
#returns back a 2d array of Tiles
def createBoard():
    id = 0; #it increments as each tile is made and serves as the id
    gameBoard = []

    # 2 for loops to create the 2d array of Tiles
    # tried doing list comprenhension but that didnt work out
    for i in range(5):
        row = []
        for j in range (5):
            row.append(Tile(i,j,id))
            id = id + 1
        gameBoard.append(row)

    return gameBoard

#=============================================================================================================
# function to set up the number of bombs on the board
#takes in the 2dArray of tiles as a argument
def createBombs( gameBoard):

    #i will need to research the ratio of bombs appearing according to the size of board
    #i will also need to use a random number generator to generate bombs in different areas

    #for now of testing purposes i will just hardcode some bombs
    #from the screenshots in the folder  bombs are at
    # [2][1]
    # [3][3]
    # [0][4]
    gameBoard[2][1].setBombStatus(True)
    gameBoard[3][3].setBombStatus(True)
    gameBoard[0][4].setBombStatus(True)

    #pretend we clicked them already for testing purposes
    gameBoard[2][1].setClicked(True)
    gameBoard[3][3].setClicked(True)
    gameBoard[0][4].setClicked(True)



#==============================================================================================================
