class Player():
    """ Parameters
        ----------
        color : str
            Color of the pieces that the player plays with.
        id : int
            Identifier for a player object.
    """
    def __init__(self, color, id):
        self.__color__ = color
        self.__id__ = id
        self.__points__ = 0

    def get_color(self):
        return self.__color__
    
    def get_id(self):
        return self.__id__