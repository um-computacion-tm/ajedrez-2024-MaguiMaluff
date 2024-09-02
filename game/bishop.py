from game.pieces import Pieces
from game.exceptions import InvalidMove

class Bishop(Pieces):
    """ Represents a Bishop chess piece, inheriting from the Pieces class."""

    def movement(self, new_position):
        """ Determines if the Bishop's move is valid and returns the path it follows.
        The Bishop can only move diagonally. If the move is valid, it returns the path
        the Bishop takes to reach the new position.
        
        Parameters
        ----------
        new_position : list
            The new position [row, column] the Bishop is moving to.
        
        Returns
        -------
        squares : list
            A list of positions the Bishop passes through if the move is valid.
        
        Raises
        ------
        InvalidMove
            If the move is not valid.
        """
        try:
            squares = self.diagonal(new_position)
            if not squares:
                raise InvalidMove("This is not a valid move")
            return squares
        except Exception as e:
            raise