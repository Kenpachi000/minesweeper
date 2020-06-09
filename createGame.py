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
    for i in range(10):
        row = []
        for j in range (10):
            row.append(Tile(i,j,id))
            id = id + 1
        gameBoard.append(row)

    return gameBoard

#=============================================================================================================
# function









#==============================================================================================================
