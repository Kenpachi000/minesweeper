"""
Essentially the Central Hub thing indicated in the UML diagram

For now we will keep everything printed to terminal and eventually make a gui using tkinter

For now we will keep the size of the minesweep board to a fix size and later change it
depending on the userinput

my randomnotes:
    list passed in by argument are mutable and will reflect back

    immutable things like int,string will not reflect back

    if i pass in an object as a argument to a function, reassignging the variable to something else wont reflect back
    however changing the properties of the object will reflect back

"""

#import the Tile class from the Tile.py
from Tile import Tile
import createGame as cg

#helper function to keep printing out the board to terminal
def printEntireBoard(gameBoard):
    for i in range (5):
        for j in range (5):
            gameBoard[i][j].printImage()
        print()

def main ( ):

    gameBoard = cg.createBoard()
    cg.createBombs(gameBoard)
    printEntireBoard(gameBoard)






if __name__ == '__main__': main()
