from game.pieces import Pieces
from game.exceptions import InvalidMove

class Rook(Pieces):
    """ Represents a Rook chess piece, inheriting from the Pieces class."""

    def movement(self, new_position):
        """ Determines if the Rook's move is valid and returns the path it follows.
            The Rook can only move in straight lines (either in the same row or
            column). If the move is not valid, an exception is raised.

        Parameters
        ----------
        new_position : list
            The new position [row, column] the Rook is moving to.
        
        Returns
        -------
        squares : list
            A list of positions the Rook passes through in a straight line.
        
        Raises
        ------
        InvalidMove
            If the move is not valid.
        """
        try:
            squares = self.straight_line(new_position)
            if not squares:
                raise InvalidMove("This is not a valid move")
            return squares
        except Exception as e:
            raise
