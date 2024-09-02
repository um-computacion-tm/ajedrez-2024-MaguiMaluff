from game.exceptions import LimitedMove, InvalidMove, OutOfBoard
from emoji import emojize


class Pieces():
    """ Represents a chess piece with attributes like name, color, and position.
    
    Attributes
    ----------
    piece : str
        The name of the chess piece.
    color : str
        The color of the chess piece.
    initial_position : list
        The initial position of the piece on the board [row, column]."""
    
    def __init__(self, piece, color, initial_position):
        self.__name__ = piece
        self.__color__ = color
        self.__position__ = initial_position
        self.__image__ = None
        self.set_images()
    
    def set_images(self):
        """ Sets the emoji representation of the piece based on its color."""
        images_white = {
                        'Queen': emojize(':crown:'), 'King': emojize(':elf:'), 'Pawn' : emojize(':nose:'),
                        'Knight': emojize(':unicorn:'), 'Rook': emojize(':moai:'), 'Bishop' : emojize(':trident_emblem:')
                        }
        images_black = {
                        'Queen': emojize(':blossom:'), 'King': emojize(':prince:'),'Pawn' : emojize(':bust_in_silhouette:'),
                        'Knight': emojize(':horse_face:'), 'Rook': emojize(':office_building:'), 'Bishop' : emojize(':maple_leaf:')
                        }
        if self.__color__ == 'w':
            self.__image__ = images_white[self.__name__]
        elif self.__color__ == 'b':
            self.__image__ = images_black[self.__name__]
    
    def change_position(self, new_position):
        """ Updates the position of the piece on the board.
        
        Parameters
        ----------
        new_position : list
            The new position [row, column] of the piece on the board."""
        
        self.__position__ = new_position

    def straight_line(self, new_position):
        """ Checks if the piece is moving in a straight line. A movement 
            is straight if either the row or column remains constant. If 
            the row is constant, calls for straight_row, if the column is constant
            calls for straight column. If both are different, returns False.
        
        Parameters
        ----------
        new_position : list
            The new position [row, column] the piece is moving to. """

        row = self.__position__[0]
        column = self.__position__[1]
        if row != new_position[0] and column != new_position[1]:
            return False
        elif row == new_position[0]:
            squares = self.straight_row(row, column, new_position)
            return squares
        elif column == new_position[1]:
            squares = self.straight_column(row, column, new_position)
            return squares
    
    def straight_row(self, row, column, new_position):
        """ Generates a list of positions for a straight row movement.
        
        Parameters
        ----------
        row : int
            The current row of the piece.
        column : int
            The current column of the piece.
        new_position : list
            The new position [row, column] the piece is moving to."""
        
        squares = []
        if column < new_position[1]:
            for i in range(new_position[1] - column):
                squares.append([row, column + i + 1])
        elif column > new_position[1]:
            for i in range(column - new_position[1]):
                squares.append([row, column - i - 1])
        return squares
    
    def straight_column(self, row, column, new_position):
        """ Generates a list of positions for a straight column movement.
        
        Parameters
        ----------
        row : int
            The current row of the piece.
        column : int
            The current column of the piece.
        new_position : list
            The new position [row, column] the piece is moving to."""
        
        squares = []
        if row < new_position[0]:
            for x in range(new_position[0] - row):
                squares.append([row + x + 1, column])
        elif row > new_position[0]:
            for x in range(row - new_position[0]):
                squares.append([row - x - 1, column])
        return squares
    

    def diagonal(self, new_position):
        """ Checks if the piece is moving diagonally. A movement 
            is diagonal if both row and column change. If both are different,
            calls for type_move, and then calls the function type_move returns.
            Then checks if the last element on squares is equal to the new position,
            if not, returns False, else returns the list of squares..
        
        Parameters
        ----------
        new_position : list
            The new position [row, column] the piece is moving to."""

        row = self.__position__[0]
        column = self.__position__[1]
        if row != new_position[0] and column != new_position[1]:
            type_move = self.check_type_diagonal(row, column, new_position)
            move_function = getattr(self, type_move)
            squares = move_function(row, column, new_position)
            if squares[-1] == new_position:
                return squares
            else:
                return False
        else:
            return False
    
    def check_type_diagonal(self, row, column, new_position):
        """ Determines the type of diagonal movement. Depending on how the 
            row and column change, returns the name of the function that should
            be called to get the positions.
        
        Parameters
        ----------
        row : int
            The current row of the piece.
        column : int
            The current column of the piece.
        new_position : list
            The new position [row, column] the piece is moving to."""

        if row > new_position[0] and column > new_position[1]:
            return "left_up"
        elif row > new_position[0] and column < new_position[1]:
            return "right_up"
        elif row < new_position[0] and column > new_position[1]:
            return "left_down"
        elif row < new_position[0] and column < new_position[1]:
            return "right_down"

    def right_down(self,row, column, new_position):
        """ Generates a list of positions for a right-down diagonal movement.
        
        Parameters
        ----------
        row : int
            The current row of the piece.
        column : int
            The current column of the piece.
        new_position : list
            The new position [row, column] the piece is moving to."""
        
        squares = []
        for i in range(new_position[0] - row):
                row += 1
                column += 1
                squares.append([row, column])
        return squares
    
    def right_up(self,row, column, new_position):
        """ Generates a list of positions for a right-up diagonal movement.
        
        Parameters
        ----------
        row : int
            The current row of the piece.
        column : int
            The current column of the piece.
        new_position : list
            The new position [row, column] the piece is moving to."""
        
        squares = []
        for i in range(new_position[1] - column):
                row -= 1
                column += 1
                squares.append([row, column])
        return squares
    
    def left_down(self, row, column, new_position):
        """ Generates a list of positions for a left-down diagonal movement.
        
        Parameters
        ----------
        row : int
            The current row of the piece.
        column : int
            The current column of the piece.
        new_position : list
            The new position [row, column] the piece is moving to."""
        

        squares = []
        for i in range(new_position[0] - row):
            row += 1
            column -= 1
            squares.append([row, column])
        return squares
    
    def left_up(self,row, column, new_position):
        """ Generates a list of positions for a left-up diagonal movement.
        
        Parameters
        ----------
        row : int
            The current row of the piece.
        column : int
            The current column of the piece.
        new_position : list
            The new position [row, column] the piece is moving to."""

        squares = []
        for i in range(row - new_position[0]):
            row -= 1
            column -= 1
            squares.append([row, column])
        return squares
    
    
    def valid_or_invalid(self, new_position):
        """ Determines if the move is valid based on the piece's movement
            rules. The move is valid if it's either a straight or diagonal movement.

        Parameters
        ----------
        new_position : list
            The new position [row, column] the piece is moving to.

        Raises
        ------
        InvalidMove
            If the move is not valid (i.e., neither straight nor diagonal)."""
        
        straight = self.straight_line(new_position)
        diagonal = self.diagonal(new_position)
        if diagonal == straight:
            raise InvalidMove("This is not a valid move")
        elif diagonal != False:
            return diagonal
        elif straight != False:
            return straight
    
    def movement(self):
        pass
    




    


    




