from game.board import Board
from game.player import Player
from game.exceptions import WrongPiece, OutOfBoard, NotAnOption, InvalidPiece
from game.pieces import Pieces, Rook, Queen, Bishop, Knight
from emoji import emojize

class Chess():
    def __init__(self):
        self.__board__ = Board()
        self.__board__.set_piece_cell_begining()
        self.__player_1__ = Player('w', 1)
        self.__player_2__ = Player('b', 2)
        self.__turn__ = 1
        self.__player__ = self.__player_1__
        self.__playing__ = True
        self.__number__ = 0

    def is_playing(self):
        return self.__playing__
    
    def move_piece_board(self, piece, new_position):
        if piece.__color__ == self.__player__.__color__:
            try:
                finished = self.end_king(new_position)
                self.__board__.move_piece(piece, new_position)
                if piece.__name__ == 'Pawn':
                    self.change_pawn(piece, new_position)
                if finished:
                    self.end_game('y')
                    return False
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
        self.__number__ += 1

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
            self.msg()
        elif end.lower() != 'n':
            raise NotAnOption
    
    def check_ending(self):
        left_pieces = 0
        if self.__number__ > 32:
            for i in self.__board__.__grid__:
                for x in i:
                    if x.__state__ == False:
                        left_pieces += 1
            if left_pieces <= 1:
                self.end_game('y')
    
    def end_king(self, new_position):
        row = new_position[0]
        col = new_position[1]
        cell = self.__board__.__grid__[row][col]
        if cell.__state__ == False:
            if cell.__piece__.__name__ == "King":
                return True
            else:
                return False
        
    def msg(self):
        print('End of game!')
        print('Player: ', self.__player__.__id__, ' wins!')

    def print_turn(self):
        color = None
        if self.__player__.__color__ == 'w': 
            color = 'White'
        elif self.__player__.__color__ == 'b':
            color = 'Black'
        print("Turn --> Player: ", self.__turn__, color)
    
    def print_board(self):
        self.__board__.print_board()
    
    def print_pieces(self):
        print('White Pieces: ',  '  Black Pieces: ', '\n')
        print(' Queen: ', emojize(':crown:'), '      Queen: ', emojize(':blossom:'),'\n',
              'King:  ', emojize(':elf:'), '      King:  ', emojize(':prince:'),'\n',
              'Pawn:  ', emojize(':nose:'), '      Pawn:  ' , emojize(':bust_in_silhouette:'),'\n',
              'Knight:', emojize(':unicorn:'), '      Knight:' , emojize(':horse_face:'),'\n',
              'Rook:  ', emojize(':moai:'), '      Rook:  ', emojize(':office_building:'),'\n',
              'Bishop:', emojize(':trident_emblem:'), '      Bishop:' , emojize(':maple_leaf:'),'\n')
                        
    def print_all(self):
        self.print_pieces()
        self.print_board()
        self.print_turn()
    
    def change_pawn(self, piece, new_position):
        if piece.change_pawn():
            print('You`ve reach the end')
            print('Choose between: Rook, Bishop, Knight and Queen')
            new_piece = str(input('Which piece do you want?: ')).title()
            if new_piece in ['Rook', 'Bishop', 'Knight', 'Queen']:
                new_class = globals()[new_piece]
                color = self.__player__.__color__
                new_piece = new_class(new_piece, color, new_position)
                cell = self.__board__.get_cell(new_position)
                self.__board__.eat_piece(new_piece, new_position, cell)
            else:
                raise InvalidPiece
                


    
