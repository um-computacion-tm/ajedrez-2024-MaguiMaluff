from game.exceptions import LimitedMove, InvalidMove, OutOfBoard


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
    
    def diagonal(self, new_position):
        ini_position = []
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
        if row > new_position[0] and column > new_position[1]:
            return "left_up"
        elif row > new_position[0] and column < new_position[1]:
            return "right_up"
        elif row < new_position[0] and column > new_position[1]:
            return "left_down"
        elif row < new_position[0] and column < new_position[1]:
            return "right_down"


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

        
    def valid_or_invalid(self, new_position):
        straight = self.straight_line(new_position)
        diagonal = self.diagonal(new_position)
        if diagonal == straight:
            raise InvalidMove()
        elif diagonal != False:
            return diagonal
        elif straight != False:
            return straight
              
    def on_board(self, new_position):
        x = new_position[0]
        y = new_position[1]
        if x < 0 or x > 7:
            raise OutOfBoard()
        elif y < 0 or y > 7:
            raise OutOfBoard()

class Queen(Pieces):
    def movement(self, new_position):
        try:
            self.on_board(new_position)
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
            raise LimitedMove()
        
    def movement(self, new_position):
        try:
            self.on_board(new_position)
            self.limit(new_position)
            squares = self.valid_or_invalid(new_position)
            return squares
        except Exception as e:
            raise

class Rook(Pieces):
    def movement(self, new_position):
        try:
            self.on_board(new_position)
            squares = self.straight_line(new_position)
            return squares
        except Exception as e:
            raise

class Bishop(Pieces):
    def movement(self, new_position):
        try:
            self.on_board(new_position)
            squares = self.diagonal(new_position)
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
        elif self.__color__ == 'b':
            list = [[row - 1, column + 1],
                    [row - 1, column],
                    [row - 1, column - 1]]
        
        if new_position not in list:
            raise LimitedMove()

    def movement(self, new_position):
        try:
            self.on_board(new_position)
            squares = self.valid_or_invalid(new_position)
            self.limit(new_position)
            return squares
        except Exception as e:
            raise

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
            raise LimitedMove()
    
    def movement(self, new_position):
        try:
            self.on_board(new_position)
            self.limit(new_position)
        except Exception as e:
            raise
    


    




