# 06/08/2024

# ADDED
- Created pieces with color and position on the board
- Created class Board, with print_board(basic)
- Created Cell, with state and piece
- Created class for each piece, all of them are sons of class Pieces
- Readme

# DELETED
- Everything from branch main

# 07/08/2024

# ADDED 

- An image to each piece
- Test for Pieces

# CHANGED

- Function print_board from class Board. Now it prints the pieces in their actual place.

# 09/08/2024

# ADDED

- Added straight_line and diagonal. Checks if the movement for a piece is valid

- Class Queen, King, Bishop and Rook now verify the movement intended to make

# CREATED

- File exception

# 11/08/2024

# ADDED

- Pawn class

# 12/08/2024

# ADDED

- Class Knight

# CREATED

- move_piece and chack_squares in class Board

# CHANGED

- diagonal and straight lines, both return False if the move is invalid or a list of positions if the move is valid

# 13/08/2024

# CHANGED

- Class Pieces, functions diagonal and straight_line

# 15/08/2024

# DELETED

- Check_squares_multiple

- Check_squares_one

- Check_color

- move_piece

- eat_piece

- piece_exception

- They will be back, fixing previous functions that are not working well yet

# FIXED

- Functions diagonal, used to check only for movements to right, up or down. Now its fixed, checks for left movements as well

# 16/08/2024

# ADDED 

- check_squares_multiple/one and eat_piece, now they work

- Tests for mentioned functions

# 17/08/2024

# ADDED

- move_piece, and move, with tests

# DELETED

- move, was the same as eat_piece
