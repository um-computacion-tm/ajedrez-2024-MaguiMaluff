
    ### State = True if theres no piece or False if its occupied
    ### Piece refers to the object
class Cell():
    def __init__(self, state, piece):
        """ Parameters
            ----------
            state : bool
                True if is free, False if is not
            piece : Piece object 
                Piece belonging to the cell.
            """
        self.__state__= state
        self.__piece__ = piece

    def moved(self):
        """Changes the state of a cell that was used but is not anymore
        """
        self.__state__ = True
        self.__piece__ = None
    
    def new_piece(self, piece):
        """Changes the state of a cell is now used and assings a piece
            Parameters
            ----------
            piece : Piece object 
                Piece belonging to the cell.
        """
        self.__state__ = False
        self.__piece__ = piece