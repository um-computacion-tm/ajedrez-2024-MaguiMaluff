
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
    
    def straight_line(self, new_position):
        if self.__position__[0] != new_position[0] and self.__position__[1] != new_position[1]:
            return False

        elif self.__position__[0] == new_position[0] or self.__position__[1] == new_position[1]:
            return True
    
    def diagonal(self, new_position):
        i_position = self.__position__
        i = 0
        range = new_position[0] - i_position[0]
        if i_position[0] != new_position[0] and i_position[1] != new_position[1]:
            while i < range:
                i_position[0] += 1
                i_position[1] += 1
                i+=1
            if i_position == new_position:
                return True
            else:
                return False
        else:
            return False
    




