from game.pieces import Pieces

class Queen(Pieces):
    def movement(self, new_position):
        """ Determines if the Queen's move is valid and returns the path it follows.
            The Queen can only move in straight and diagonal lines. If the move 
            is not valid, an exception is raised.

        Parameters
        ----------
        new_position : list
            The new position [row, column] the Queen is moving to.
        
        Returns
        -------
        squares : list
            A list of positions the Queen passes through in a straight line.
        
        Raises
        ------
        InvalidMove
            If the move is not valid.
        """
        try:
            squares = self.valid_or_invalid(new_position)
            return squares
        except Exception as e:
            raise