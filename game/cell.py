
    ### State = True if theres no piece or False if its occupied
    ### Piece refers to the object
class Cell():
    def __init__(self, state, piece):
        self.__state__= state
        self.__piece__ = piece

    def moved(self):
        self.__state__ = True
        self.__piece__ = None