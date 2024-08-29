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

# ADDED

- File exception

# 11/08/2024

# ADDED

- Pawn class

# 12/08/2024

# ADDED

- Class Knight

# ADDED

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

# 18/08/2024

# ADDED

- In class Board, added knight, checks especificaly for knight movement

# 19/08/2024

# ADDED

- Function pawn in class Board, checks for the pawns movement
- Tests for pawn in board

# 20/08/2024

# ADDED

- Class Players and Tests

- Class Chess and Tests

# 21/08/2024

# ADDED

- change_cell in Board

- moved in Cell

- cli

- get_column, next_turn and is_playing in Chess

# CHANGED

- eat_piece, chages cell state to False

- end_game, now the game ends!

# 22/08/2024

# FIXED

- Error "No module named 'game'" from cli. Created a folder cli_folder

# 23/02/2024

# FIXED

- end_game, now raises an exception if the letter is not valid

# 25/08/2024

# ADDED

- end_king, check_ending and msg

# 26/08/2024

# CHANGED 

- Board, Cell, applied Single Responsability 

- eat_piece, now calls new_piece from cell insted of changing the cell itself. Same with piece position, calls change_position

- check_squares_one, check_squares_multiple, eat_piece, pawn, knight are given the cell instead of searching for it

- exceptions all around, now they return a string explaining the error


# ADDED

- New_piece on Cell

- Print_board, print_turn on chess

- on_board to Board

# FIXED

- Rook and Bishop movement

# DELETED

- on_board from Pieces

- Function knight from Board

# 27/08/2024

# ADDED

- function print_all to Chess. In charge of printing turn, board and pieces.

- Function change_pawn to Chess and Pawn. 

# CHANGED

- Images for pieces, now emojis instead of low and upper letters.

- Dockerfile

- print_pieces

- coveragerc and README

# 29/08/2024

# DELETED

- print_header from board