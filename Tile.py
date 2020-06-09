"""

Tile class which represents on single tile or square on the board

each tile will have
    -status object
    -know its location on the board
    - a special unique ID to themselves

A status object will contain what that tile is
 - bomb     (True/false)
 - number   (True/false,  that number )
 - blank    (True/false)
 - clicked / nonclicked (True / false)

and respond correctly when clicked.
"""

from Status import Status

class Tile:

    # double underscore to denote "private" variables but im just gonna keep everything public

    #out here means class variable or static variables

    #constructor
    def __init__(self, xCordinate, yCordinate, ID):
        self.xCordinate = xCordinate
        self.yCordinate = yCordinate
        self.ID = ID
        self.statusOBJ = Status()

    #helper method to print out information
    def printInfo(self):
        print("x: ", self.xCordinate)
        print("y: ", self.yCordinate)
        print("ID: ", self.ID)
        self.statusOBJ.printStatus()
        print()

    #methods that will change the status of the tile
    def setBombStatus (self, boolean):
        self.statusOBJ.setBomb(boolean)

    def setClicked(self, boolean):
        self.statusOBJ.setClicked(boolean)

    def setBlank(self, boolean):
        self.statusOBJ.setBlank(boolean)

    def setNumBomb(self, number):
        self.statusOBJ.setNumBomb(number)

    #methods that checks for information
    def checkBomb(self):
        return self.statusOBJ.checkBomb()

    def checkClicked(self):
        return self.statusOBJ.checkClicked()

    def checkBlank(self):
        return self.statusOBJ.checkBlank()

    def getNumBomb(self):
        return self.statusOBJ.getNumBomb()

    #print the image onto the terminal. will replace later with the gui
    def printImage(self):
        self.statusOBJ.printImage()
