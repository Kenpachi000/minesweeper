"""
Essentially the Central Hub thing indicated in the UML diagram

For now we will keep everything printed to terminal and eventually make a gui using tkinter

For now we will keep the size of the minesweep board to a fix size and later change it
depending on the userinput

"""

#import the Tile class from the Tile.py
from Tile import Tile


def main ( ):

    count = 0

    #below creates a 2d array of Tiles
    gameBoard = []
    for i in range (5):
        row = []
        for j in range (6):
            row.append(Tile(i,j,count))
            count = count + 1;
        gameBoard.append(row)

    #print out the board in good fashion
    for i in range(5):
        for j in range (6):
            print(gameBoard[i][j].ID, ' ', end ='')
        print()

    #test to see if it lines up
    gameBoard[3][4].printInfo()




if __name__ == '__main__': main()
