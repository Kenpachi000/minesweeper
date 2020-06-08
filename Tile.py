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

class Tile:

    # double underscore to denote "private" variables but im just gonna keep everything public

    #out here means class variable or static variables
    #Status object goes here.. fill in here

    #constructor
    def __init__(self, xCordinate, yCordinate, ID):
        self.xCordinate = xCordinate
        self.yCordinate = yCordinate
        self.ID = ID

    #empty constructor used to just make an object
    # def __init__(self):
    #     pass

    #helper method to print out information
    def printInfo(self):
        print("x: ", self.xCordinate)
        print("y: ", self.yCordinate)
        print("ID: ", self.ID)
