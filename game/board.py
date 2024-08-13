from game.pieces import Pieces, Queen, King, Rook, Bishop, Knight, Pawn
from game.cell import Cell
from game.exceptions import InvalidMove

class Board():
    def __init__(self):         ### Declaracion de cada pieza, con nombre, color y posicion al inicio del juego
            self.__pieces__ = [ Queen(piece="Queen",  color="w", initial_position=[0, 3]),   Queen(piece="Queen",   color="b", initial_position=[7, 3]),
                                King(piece="King",   color="w", initial_position=[0, 4]),    King(piece="King",    color="b", initial_position=[7, 4]),
                                Rook(piece="Rook" ,  color="w", initial_position=[0, 0]),    Rook(piece="Rook",    color="b", initial_position=[7, 0]),
                                Rook(piece="Rook" ,  color="w", initial_position=[0, 7]),    Rook(piece="Rook",    color="b", initial_position=[7, 7]),
                                Bishop(piece="Bishop", color="w", initial_position=[0, 2]),  Bishop(piece="Bishop",  color="b", initial_position=[7, 2]),
                                Bishop(piece="Bishop", color="w", initial_position=[0, 5]),  Bishop(piece="Bishop",  color="b", initial_position=[7, 5]),
                                Knight(piece="Knight", color="w", initial_position=[0, 1]),  Knight(piece="Knight",  color="b", initial_position=[7, 1]),
                                Knight(piece="Knight", color="w", initial_position=[0, 6]),  Knight(piece="Knight",  color="b", initial_position=[7, 6]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 0]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 0]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 1]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 1]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 2]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 2]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 3]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 3]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 4]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 4]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 5]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 5]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 6]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 6]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 7]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 7]),]
            ### Lista de listas de 8x8
            self.__grid__ = ([[Cell(True, None) for _ in range(8)] for _ in range (8)])
            self.set_piece_cell_begining()
    

    ### Impresion del board, con las piezas en posicion actual
    def print_board(self):
        self.print_header()
        self.print_pieces()

    ### Imprime las letras de cada columna
    def print_header(self):
        print(' '+'-'*56)
        print('   {:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|'.format("", "A", "B" , "C", "D" , "E" , "F" , "G" ,"H" ))
        print(' '+'-'*56)
    
    ### Llama a print_row 8 veces
    def print_pieces(self):
        for i in range(8):
            self.print_rows(i)
            
    ### Row es una lista, a la que voy agrgando de a uno la imagen de la pieza que esta
    ### en esa posicion, si no hay pieza, no imprime nada alli.
    ### Imprime todo formateado para que se vea ordenado
    ### self.__grid__[i][x].__piece__.__image__, grid[][] me selecciona una fila y una columna
    ### donde hay una celda, .piece me llama a la pieza que esta en la celda, -image, se
    ### se refiere a la imagen de la pieza.
    def print_rows(self, i):
        row = [i] 
        for x in range(8):
                if self.__grid__[i][x].__state__ == False:
                    row.append(str(self.__grid__[i][x].__piece__.__image__))
                else:
                    row += ' '
        print('   {:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|'.format(*row))
        print(' '+'-'*56)

                

    ### Order by pieces, check the piece position, asign the 
    ### piece to the cell that belongs to the position on the grid
    ### and changes the state
    def set_piece_cell_begining(self):
        for i in self.__pieces__:
            i.set_images()
            position = i.__position__
            x = position[0]
            y = position[1]
            self.__grid__[x][y].__state__ = False
            self.__grid__[x][y].__piece__ = i

    def check_squares(self, squares):
        for square in squares:
            x = square[0]
            y = square[1]
            cell_state = self.__grid__[x][y].__state__
            if cell_state == False and [x , y] != squares[-1]:
                raise InvalidMove
    
    def check_color(self, piece, last_square):
        row = last_square[0]
        column = last_square[1]
        last_square = self.__grid__[row][column]
        if last_square.__state__ == False and piece.__color__ == last_square.__piece__.__color__:
            raise InvalidMove()
        
    ### Llama a la funcion en piece que verifica si la forma de movimiento es valida.
    ### Llamar a la funcion check_around, para saber si se puede mover a traves
    def move_piece(self, piece, new_position):
        try:
            squares = piece.movement(new_position)
            self.check_color(piece, squares[-1])
            self.check_squares(squares)
            piece.__position__ = new_position
        except Exception as e:
            raise
    

        
