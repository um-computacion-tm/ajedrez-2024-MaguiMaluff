from game.board import Board
from game.player import Player
from game.exceptions import WrongPiece, OutOfBoard

class Chess():
    def __init__(self):
        self.__board__ = Board()
        self.__board__.set_piece_cell_begining()
        self.__player_1__ = Player('w', 1)
        self.__player_2__ = Player('b', 2)
        self.__turn__ = 1
        self.__player__ = self.__player_1__
        self.__playing__ = True

    def is_playing(self):
        return self.__playing__
    
    def move_piece_board(self, piece, new_position):
        if piece.__color__ == self.__player__.__color__:
            try:
                self.__board__.move_piece(piece, new_position)
            except Exception as e:
                raise
        else:
            raise WrongPiece
    
    def get_piece(self, row, column):
        if row < 8 and column < 8 and row >= 0 and column >= 0:
            piece = self.__board__.__grid__[row][column].__piece__
            return piece
        else:
            raise OutOfBoard
    
    def next_turn(self):
        if self.__player__ == self.__player_1__:
            self.__turn__ = 2
            self.__player__ = self.__player_2__
        elif self.__player__ == self.__player_2__:
            self.__turn__ = 1
            self.__player__ = self.__player_1__

    def get_column(self, column):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        column = column.upper()
        if column in letters:
            return letters.index(column)
        else:
            raise ValueError("Invalid column letter")
        

    def end_game(self, end):
        if end.lower() == 'y':
            self.__playing__= False