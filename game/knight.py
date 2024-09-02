from game.pieces import Pieces
from game.exceptions import LimitedMove

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