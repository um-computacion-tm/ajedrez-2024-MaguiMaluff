from game.pieces import Pieces
from game.exceptions import LimitedMove

class King(Pieces):
    """ Represents a King chess piece, inheriting from the Pieces class."""

    def limit(self, new_position):
        """ Checks if the King's move is valid. The King moves exactly one square 
            in any direction.If the move is not valid, an exception is raised.
        
        Parameters
        ----------
        new_position : list
            The new position [row, column] the King is moving to.
        
        Raises
        ------
        LimitedMove
            If the move does not follow the King's single-square movement rule.
        """
        row = self.__position__[0]
        column = self.__position__[1]
        valid_moves = [[row + 1, column + 1],
                       [row + 1, column],
                       [row + 1, column - 1],
                       [row - 1, column + 1],
                       [row - 1, column],
                       [row - 1, column - 1],
                       [row, column + 1],
                       [row, column - 1]]
        
        if new_position not in valid_moves:
            raise LimitedMove("You can only move one square")

    def movement(self, new_position):
        """ Determines if the King's move is valid and returns the path it follows.
        
        Parameters
        ----------
        new_position : list
            The new position [row, column] the King is moving to.
        
        Returns
        -------
        squares : list
            A list containing the new position if the move is valid.
        
        Raises
        ------
        LimitedMove
            If the move does not follow the King's single-square movement rule.
        InvalidMove
            If the move is not valid.
        """
        try:
            self.limit(new_position)
            squares = self.valid_or_invalid(new_position)
            return squares
        except Exception as e:
            raise