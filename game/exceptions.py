class LimitedMove(Exception):           #"You can only move on square"
    pass

class InvalidMove(Exception):           #"This is not a valid move"
    pass

class OutOfBoard(Exception):            #"Please choose a valid position"
    pass

class GoingThroughAPiece(Exception):    #"Oops! You`re trying to go through a piece"
    pass

class SameColor(Exception):             #"Oops! You`re trying to eat your own piece"
    pass

class WrongPiece(Exception):            #"Oops! You`re trying to move the opponent`s Piece"
    pass

class NotAnOption(Exception):           #"Please enter y or n"
    pass

class InvalidPiece(Exception):          #"Please choose a valid Piece"
    pass