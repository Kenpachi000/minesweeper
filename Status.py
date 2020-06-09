"""
Status class which holds basic information.
This will get attached to each instance of a Tile

Couple of boolean variables

    Is it a bomb?
    Is it clicked / nonclicked?
    Is it just a blank square
    How many surrounding bombs are there?

"""

class Status:

    def __init__(self):
        self.isBomb = False
        self.isClicked = False
        self.isBlank = False
        self.numOfBombs = -999

    #methods to alternate those values
    def setBomb(self, boolean):
        self.isBomb = boolean

    def setClicked(self, boolean):
        self.isClicked = boolean

    def setBlank(self, boolean):
        self.isBlank = boolean

    def setNumBomb(self, number):
        self.numOfBombs = number

    #methods to check for information about things

    def checkBomb(self):
        return self.isBomb

    def checkClicked(self):
        return self.isClicked

    def checkBlank(self):
        return self.isBlank

    def getNumBomb(self):
        return self.numOfBombs

    # debugging information
    def printStatus(self):
        print("isBomb: ", self.isBomb)
        print("isClick: ", self.isClicked)
        print("isBlank: ", self.isBlank)
        print("numBomb: ", self.numOfBombs)


    #first we check if the tile has been clicked or not
    #once isClick becomes true we have to check which one and then print to screen accordingly
    def printImage(self):
        if self.isClicked == False:
            print(" * ", end = "") #default behavior
        elif self.isBomb == True:
            print(" b ", end = "")
        elif self.isBlank == True:
            print (" $ ", end = "")
        else:
            print(" ", self.numOfBombs, " ", end = "")
