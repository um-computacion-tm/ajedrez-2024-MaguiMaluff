from game.exceptions import LimitedMove, InvalidMove, OutOfBoard
from emoji import emojize


class Pieces(): ###Color = black or white, Piece = Queen, King, Pawn, Rook, Bishop, Knight, Position = [row , column]
    def __init__(self, piece, color, initial_position):
        self.__name__ = piece
        self.__color__ = color
        self.__position__ = initial_position
        self.__image__ = None
        self.set_images()
    
    def set_images(self):
        images_white = {
                        'Queen': emojize(':crown:'),
                        'King': emojize(':elf:'),
                        'Pawn' : emojize(':nose:'),
                        'Knight': emojize(':unicorn:'),
                        'Rook': emojize(':moai:'),
                        'Bishop' : emojize(':trident_emblem:')
                        }
        images_black = {
                        'Queen': emojize(':blossom:'),
                        'King': emojize(':prince:'),
                        'Pawn' : emojize(':bust_in_silhouette:'),
                        'Knight': emojize(':horse_face:'),
                        'Rook': emojize(':office_building:'),
                        'Bishop' : emojize(':maple_leaf:')
                        }
        if self.__color__ == 'w':
            self.__image__ = images_white[self.__name__]
        elif self.__color__ == 'b':
            self.__image__ = images_black[self.__name__]
    
    def change_position(self, new_position):
        self.__position__ = new_position

    ### Checks if the movement is straight. If the column or row doesnt change,
    ### its moving in a straight line
    def straight_line(self, new_position):
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
    
    ### Makes a list with each position the piece goes
    ### to before getting to the new position.
    def straight_row(self, row, column, new_position):
        squares = []
        if column < new_position[1]:
            for i in range(new_position[1] - column):
                squares.append([row, column + i + 1])
        elif column > new_position[1]:
            for i in range(column - new_position[1]):
                squares.append([row, column - i - 1])
        return squares
    
    def straight_column(self, row, column, new_position):
        squares = []
        if row < new_position[0]:
            for x in range(new_position[0] - row):
                squares.append([row + x + 1, column])
        elif row > new_position[0]:
            for x in range(row - new_position[0]):
                squares.append([row - x - 1, column])
        return squares
    
    ### Checks if the movement is diagonal, both row and column
    ### should be atleast different. Then calls for check type diagonal 
    def diagonal(self, new_position):
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
    
    ### Depending on how the row and column changes, it returns a
    ### string with the name of the function that should be call
    ### to get the positions
    def check_type_diagonal(self, row, column, new_position):
        if row > new_position[0] and column > new_position[1]:
            return "left_up"
        elif row > new_position[0] and column < new_position[1]:
            return "right_up"
        elif row < new_position[0] and column > new_position[1]:
            return "left_down"
        elif row < new_position[0] and column < new_position[1]:
            return "right_down"

    ### Makes a list with each position the piece goes
    ### to before getting to the new position.
    def right_down(self,row, column, new_position):
        squares = []
        for i in range(new_position[0] - row):
                row += 1
                column += 1
                squares.append([row, column])
        return squares
    
    def right_up(self,row, column, new_position):
        squares = []
        for i in range(new_position[1] - column):
                row -= 1
                column += 1
                squares.append([row, column])
        return squares
    
    def left_down(self, row, column, new_position):
        squares = []
        for i in range(new_position[0] - row):
            row += 1
            column -= 1
            squares.append([row, column])
        return squares
    
    def left_up(self,row, column, new_position):
        squares = []
        for i in range(row - new_position[0]):
            row -= 1
            column -= 1
            squares.append([row, column])
        return squares
    
    ### A movement cant be diagonal and straight or none at the same time
    ### (only exception would be knight)
    def valid_or_invalid(self, new_position):
        straight = self.straight_line(new_position)
        diagonal = self.diagonal(new_position)
        if diagonal == straight:
            raise InvalidMove("This is not a valid move")
        elif diagonal != False:
            return diagonal
        elif straight != False:
            return straight
        
class Queen(Pieces):
    def movement(self, new_position):
        try:
            squares = self.valid_or_invalid(new_position)
            return squares
        except Exception as e:
            raise
    
class King(Pieces):
    def limit(self, new_position):
        row = self.__position__[0]
        column = self.__position__[1]
        list = [[row + 1, column + 1],
                [row + 1, column],
                [row + 1, column - 1],
                [row - 1, column + 1],
                [row - 1, column],
                [row - 1, column - 1],
                [row, column + 1],
                [row, column - 1]]
        
        if new_position not in list:
            raise LimitedMove("You can only move on square")
        
    def movement(self, new_position):
        try:
            self.limit(new_position)
            squares = self.valid_or_invalid(new_position)
            return squares
        except Exception as e:
            raise

class Rook(Pieces):
    def movement(self, new_position):
        try:
            squares = self.straight_line(new_position)
            if not squares:
                raise InvalidMove("This is not a valid move")
            return squares
        except Exception as e:
            raise

class Bishop(Pieces):
    def movement(self, new_position):
        try:
            squares = self.diagonal(new_position)
            if not squares:
                raise InvalidMove("This is not a valid move")
            return squares
        except Exception as e:
            raise

class Pawn(Pieces):
    def limit(self, new_position):
        row = self.__position__[0]
        column = self.__position__[1]
        if self.__color__ == 'w':
            list = [[row + 1, column + 1],
                    [row + 1, column],
                    [row + 1, column - 1]]
            if row == 1:
                list.append([row + 2, column])

        elif self.__color__ == 'b':
            list = [[row - 1, column + 1],
                    [row - 1, column],
                    [row - 1, column - 1]]
            if row == 6:
                list.append([row - 2, column])
        
        if new_position not in list:
            raise LimitedMove("You can only move on square")

    def movement(self, new_position):
        try:
            squares = self.valid_or_invalid(new_position)
            self.limit(new_position)
            return squares
        except Exception as e:
            raise
    
    ### A pawn can change to another piece (excluding King),
    ### when it reaches the other side of the board
    def change_pawn(self):
        if self.__position__[0] == 7 and self.__color__ == 'w':
            return True
        elif self.__position__[0] == 0 and self.__color__ == 'b':
            return True
        else:
            return False

class Knight(Pieces):
    def limit(self, new_position):
        row = self.__position__[0]
        column = self.__position__[1]
        list = [[row - 2, column - 1],
                [row - 2, column + 1],
                [row - 1, column - 2],
                [row - 1, column + 2],
                [row + 1, column - 2],
                [row + 1, column + 2],
                [row + 2, column - 1],
                [row + 2, column + 1]]
        
        if new_position not in list:
            raise LimitedMove("You can only move in an L shape")
    
    def movement(self, new_position):
        try:
            self.limit(new_position)
            return([new_position])
        except Exception as e:
            raise
    


    




