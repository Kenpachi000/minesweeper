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

def createTheBord(gameBoard):
    count = 0
    for i in range(5):
        row = []
        for j in range(6):
            row.append(Tile(i,j,count))
            count = count + 1
        gameBoard.append(row)

def changeValues(TileOBJECT):
    TileOBJECT.setBombStatus(True) #changes reflect back

    TileOBJECT = 10 #changes wont reflect 




def main ( ):

    t1 = Tile(1,1,1)
    changeValues(t1)
    t1.printInfo()





    #count = 0

    #below creates a 2d array of Tiles
    # gameBoard = []
    # createTheBord(gameBoard)

    # #print out the board in good fashion
    # for i in range(5):
    #     for j in range (6):
    #         print(gameBoard[i][j].ID, ' ', end ='')
    #     print()

    #test to see if it lines up
    # gameBoard[3][4].setNumBomb(3)
    # gameBoard[3][4].printInfo()
    #
    # gameBoard[1][1].setBombStatus(True)
    # gameBoard[1][1].setBlank(True)
    # gameBoard[1][1].printInfo()




if __name__ == '__main__': main()
