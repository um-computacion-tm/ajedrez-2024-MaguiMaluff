from game.pieces import Pieces
from game.exceptions import LimitedMove

class Pawn(Pieces):
    """Represents a Pawn chess piece, inheriting from the Pieces class."""

    def limit(self, new_position):
        """ Checks if the Pawn's move is within its allowed movement limits.
            The Pawn can move one square forward, and optionally two squares forward
            from its starting position. It can also capture diagonally.
            The limits are different for white and black Pawns.
        
        Parameters
        ----------
        new_position : list
            The new position [row, column] the Pawn is moving to.
        
        Raises
        ------
        LimitedMove
            If the move is not within the Pawn's allowed movement range.
        """
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
        """ Determines if the Pawn's move is valid and returns the path it follows.
            The Pawn can move straight or diagonally, but only one square (2 if its 
            the first move). 

        Parameters
        ----------
        new_position : list
            The new position [row, column] the Pawn is moving to.
        
        Returns
        -------
        square : list
            A list of positions the Pawn passes through.
        
        Raises
        ------
        LimitedMove
            If the move is not within the Pawn's allowed movement range.
        InvalidMove
            If the move is not valid according to general movement rules.
        """
        try:
            squares = self.valid_or_invalid(new_position)
            self.limit(new_position)
            return squares
        except Exception as e:
            raise
    
    def change_pawn(self):
        """ Checks if the Pawn has reached the end. If it reaches the 
            opposite end of the board it can be change to another piece.
        
        Returns
        -------
        bool
            True if the Pawn is at the end, False otherwise.
        """
        if self.__position__[0] == 7 and self.__color__ == 'w':
            return True
        elif self.__position__[0] == 0 and self.__color__ == 'b':
            return True
        else:
            return False
