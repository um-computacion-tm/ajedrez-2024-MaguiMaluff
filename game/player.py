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
