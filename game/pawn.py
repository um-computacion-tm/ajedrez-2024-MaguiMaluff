from game.pieces import Pieces
from game.exceptions import LimitedMove

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
    
    def change_pawn(self):
        if self.__position__[0] == 7 and self.__color__ == 'w':
            return True
        elif self.__position__[0] == 0 and self.__color__ == 'b':
            return True
        else:
            return False
