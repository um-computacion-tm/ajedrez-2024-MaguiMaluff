
class Pieces(): ###Color = black or white, Piece = Queen, King, Pawn, Rook, Bishop, Knight, Position = (row , column)
    def __init__(self, piece, color, initial_position):
        self.__name__ = piece
        self.__color__ = color
        self.__position__ = initial_position

"""class Queen(Pieces):
    def __init__(self):
        pass
    def movement(self):
        pass

class King(Pieces):
    def __init__(self):
        pass
    def movement(self):
        pass

class Bishop(Pieces):
    def __init__(self):
        pass
    def movement(self):
        pass

class Knight(Pieces):
    def __init__(self):
        pass
    def movement(self):
        pass

class Rook(Pieces):
    def __init__(self):
        pass
    def movement(self):
        pass

class Pawn(Pieces):
    def __init__(self):
        pass
    def movement(self):
        pass"""