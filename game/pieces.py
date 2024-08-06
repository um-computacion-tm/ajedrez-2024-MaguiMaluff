
class Pieces(): ###Color = black or white, Piece = Queen, King, Pawn, Rook, Bishop, Knight, Position = (row , column)
    def __init__(self, color, piece, initial_position):
        self.__piece__ = piece
        self.__color__ = color
        self.__position__ = initial_position

