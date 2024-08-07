class Pieces(): ###Color = black or white, Piece = Queen, King, Pawn, Rook, Bishop, Knight, Position = (row , column)
    def __init__(self, piece, color, initial_position):
        self.__name__ = piece
        self.__color__ = color
        self.__position__ = initial_position
        self.__image__ = None
    
    def set_images(self):
        images_white = {
                        'Queen': '♛',
                        'King': '♚',
                        'Pawn' : '♗',
                        'Knight': '♞',
                        'Rook': '♜',
                        'Bishop' : '♝'
                        }
        images_black = {
                        'Queen': '♕',
                        'King': '♔',
                        'Pawn' : '♙',
                        'Knight': '♘',
                        'Rook': '♖',
                        'Bishop' : '♗'
                        }
        if self.__color__ == 'w':
            self.__image__ = images_white[self.__name__]
        elif self.__color__ == 'b':
            self.__image__ = images_black[self.__name__]            

