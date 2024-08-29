from game.board import Board
from game.player import Player
from game.exceptions import WrongPiece, OutOfBoard, NotAnOption, InvalidPiece
from game.pieces import Pieces, Rook, Queen, Bishop, Knight
from emoji import emojize

class Chess():
    """ A class that represents the game and communicates between cli and the other classes.

        Attributes
        ----------

        __board__ : Board object
            Initializes and instance of the class Board.
        __player_1__ : Player object
            Player that plays with white.
        __player_2__ : Player object
            Player that plays with black.
        __turn__ : int
            Initializes on 1, varies between 1 and 2, depending on the player playing.
        __player__ : Player object
            Player that is actually playing (__player_1__, __player_2__)
        __playing__ : Bool
            Is the game is being played this variable is True, if  it ends, its False
        __number__ : int
            Starts at 0, increase by 1 every turn.

    """
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
        """Returns the value of __playing__"""
        return self.__playing__
    
    def move_piece_board(self, piece, new_position):
        """ Calls fot the necesary functions to move a piece.

            Parameters
            ----------
            piece : Piece object
                Piece that is intended to move
            new_position : list
                Coordinates for the position the piece is going to be moved to

            Raises
            ------
            WrongPiece
                If the player's color is different than the piece's color, then
                the player can't move that piece

        """
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
            raise WrongPiece("Oops! You're trying to move the opponent's Piece")
    
    def get_piece(self, row, column):
        """ Gets the piece that is in a given row and column, if there's no piece,
            raises an exception.

            Parameters
            ----------
            row : int
                Row on the board's grid.
            column : int
                Column on the board's grid.

            Raises
            ------
            WrongPiece
                When the row and column doesn't have a piece.
            OutOfBoard
                When the row and column are greater or equal to 8 or less than 0.
        """
        if row < 8 and column < 8 and row >= 0 and column >= 0:
            piece = self.__board__.get_piece([row, column])
            if piece:
                return piece
            else:
                raise WrongPiece("There's no piece there!")
        else:
            raise OutOfBoard("Please choose a valid position")
    
    def next_turn(self):
        """ If the ___player___ playing is __player_1__, the the next turn goes to
            __player_2__ and __turn__ is 2. If the ___player___ playing is __player_2__,
            the the next turn goes to __player_1__ and __turn__ is 1.
        """
        if self.__player__ == self.__player_1__:
            self.__turn__ = 2
            self.__player__ = self.__player_2__
        elif self.__player__ == self.__player_2__:
            self.__turn__ = 1
            self.__player__ = self.__player_1__
        self.__number__ += 1

    def get_column(self, column):
        """ Columns are given in letters, if the column is in the list, the it returns
            the list index for that letter.

            Parameters
            ----------
            column : str
                A letter tha coresponds to a column.
            
            Raises
            ------
            ValueError
                If the column is not in the list.
        """
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        column = column.upper()
        if column in letters:
            return letters.index(column)
        else:
            raise ValueError("Invalid column letter")
        
    def end_game(self, end):
        """Ends the game if end is y.

            Parameters
            ----------
            end : str
                y or no, y for yes, n for n.
            
            Raises
            ------
            NotAnOption
                When end is something else tha y or n.
        """
        if end.lower() == 'y':
            self.__playing__= False
            self.msg()
        elif end.lower() != 'n':
            raise NotAnOption("Please enter y or n")
    
    def check_ending(self):
        """ Once the number of plays is greater than 32, it counts the pieces
            left on the board. If the sum is equal or less than 1, the game ends.
        """
        left_pieces = 0
        if self.__number__ > 32:
            for i in self.__board__.__grid__:
                for x in i:
                    if x.__state__ == False:
                        left_pieces += 1
            if left_pieces <= 1:
                self.end_game('y')
    
    def end_king(self, new_position):
        """ Checks if the King is being capture. Returns True if it is,
            and False if its not.

            Parameters
            ----------
            new_position : list
                Coordenates to the position a piece is trying to move to. 
        """
        row = new_position[0]
        col = new_position[1]
        cell = self.__board__.get_cell([row, col])
        if cell.__state__ == False:
            if cell.__piece__.__name__ == "King":
                return True
            else:
                return False
        
    def msg(self):
        """ Prints a message for the end of the game.
        """
        print('End of game!')
        print('Player: ', self.__player__.__id__, ' wins!')

    def print_turn(self):
        """ Prints the turn, id from the player and color.
        """
        color = None
        if self.__player__.__color__ == 'w': 
            color = 'White'
        elif self.__player__.__color__ == 'b':
            color = 'Black'
        print("Turn --> Player: ", self.__turn__," Color: ", color)
    
    def print_board(self):
        """ Calls for print_board.
        """
        self.__board__.print_board()
    
    def print_pieces(self):
        """ Prints the pieces images.
        """
        print('White Pieces: ',  '  Black Pieces: ', '\n')
        print(' Queen: ', emojize(':crown:'), '      Queen: ', emojize(':blossom:'),'\n',
              'King:  ', emojize(':elf:'), '      King:  ', emojize(':prince:'),'\n',
              'Pawn:  ', emojize(':nose:'), '      Pawn:  ' , emojize(':bust_in_silhouette:'),'\n',
              'Knight:', emojize(':unicorn:'), '      Knight:' , emojize(':horse_face:'),'\n',
              'Rook:  ', emojize(':moai:'), '      Rook:  ', emojize(':office_building:'),'\n',
              'Bishop:', emojize(':trident_emblem:'), '      Bishop:' , emojize(':maple_leaf:'),'\n')
                        
    def print_all(self):
        """ Calls for every print function.
        """
        self.print_pieces()
        self.print_board()
        self.print_turn()
    
    def change_pawn(self, piece, new_position):
        """ When a Pawn reaches the other end, it can be change to another piece.
            calls for change_pawn() (in charge of verificating if the pawn is in the correct end).
            If it is, asks for the new piece, looks for it in a list, and if it is there then the
            change is made, creating a new piece.

            Parameters
            ----------
            piece : Pawn Object
                Pawn that could be at an end.
            new_position : list
                Coordinates for the position the pawn has already moved to.
            
            Raises
            ------
            InvalidPiece
                When the piece given to chaged to is not in the list.
        """
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
                raise InvalidPiece("Please choose a valid Piece")
                


    
