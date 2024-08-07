class Pieces(): ###Color = black or white, Piece = Queen, King, Pawn, Rook, Bishop, Knight, Position = (row , column) ♜
    def __init__(self, piece, color, initial_position):
        self.__name__ = piece
        self.__color__ = color
        self.__position__ = initial_position
        self.__image__ = None
    
    def set_images(self):
        images_white = {
                        'Queen': 'q',
                        'King': 'k',
                        'Pawn' : 'p',
                        'Knight': 'n',
                        'Rook': 'r',
                        'Bishop' : 'b'
                        }
        images_black = {
                        'Queen': 'Q',
                        'King': 'K',
                        'Pawn' : 'P',
                        'Knight': 'N',
                        'Rook': 'R',
                        'Bishop' : 'B'
                        }
        if self.__color__ == 'w':
            self.__image__ = images_white[self.__name__]
        elif self.__color__ == 'b':
            self.__image__ = images_black[self.__name__]            

