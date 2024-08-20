from game.board import Board
from game.player import Player
from game.exceptions import WrongPiece, OutOfBoard

class Chess():
    def __init__(self):
        self.__board__ = Board()
        self.__board__.set_piece_cell_begining()
        player_1 = Player('w', 1)
        player_2 = Player('b', 2)
        self.__turn__ = player_1
    
    def move_piece_board(self, piece, new_position):
        if piece.__color__ == self.__turn__.__color__:
            self.__board__.move_piece(piece, new_position)
        else:
            raise WrongPiece
    
    def get_piece(self, row, column):
        if row < 8 and column < 8 and row >= 0 and column >= 0:
            piece = self.__board__.__grid__[row][column].__piece__
            return piece
        else:
            raise OutOfBoard
    
    def end_game(self):
        return False