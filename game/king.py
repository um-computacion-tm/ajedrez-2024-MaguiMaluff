from game.pieces import Pieces
from game.exceptions import LimitedMove

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