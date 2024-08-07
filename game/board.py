from game.pieces import Pieces
from game.cell import Cell

class Board():
    def __init__(self):         ### Declaracion de cada pieza, con nombre, color y posicion al inicio del juego
            self.__pieces__ = [ Pieces(piece="Queen",  color="w", initial_position=(0, 3)),  Pieces(piece="Queen",   color="b", initial_position=(7, 3)),
                                Pieces(piece="King",   color="w", initial_position=(0, 4)),  Pieces(piece="King",    color="b", initial_position=(7, 4)),
                                Pieces(piece="Rook" ,  color="w", initial_position=(0, 0)),  Pieces(piece="Rook",    color="b", initial_position=(7, 0)),
                                Pieces(piece="Rook" ,  color="w", initial_position=(0, 7)),  Pieces(piece="Rook",    color="b", initial_position=(7, 7)),
                                Pieces(piece="Bishop", color="w", initial_position=(0, 2)),  Pieces(piece="Bishop",  color="b", initial_position=(7, 2)),
                                Pieces(piece="Bishop", color="w", initial_position=(0, 5)),  Pieces(piece="Bishop",  color="b", initial_position=(7, 5)),
                                Pieces(piece="Knight", color="w", initial_position=(0, 1)),  Pieces(piece="Knight",  color="b", initial_position=(7, 1)),
                                Pieces(piece="Knight", color="w", initial_position=(0, 6)),  Pieces(piece="Knight",  color="b", initial_position=(7, 6)),
                                Pieces(piece="Pawn" ,  color="w", initial_position=(1, 0)),  Pieces(piece="Pawn" ,   color="b", initial_position=(6, 0)),
                                Pieces(piece="Pawn" ,  color="w", initial_position=(1, 1)),  Pieces(piece="Pawn" ,   color="b", initial_position=(6, 1)),
                                Pieces(piece="Pawn" ,  color="w", initial_position=(1, 2)),  Pieces(piece="Pawn" ,   color="b", initial_position=(6, 2)),
                                Pieces(piece="Pawn" ,  color="w", initial_position=(1, 3)),  Pieces(piece="Pawn" ,   color="b", initial_position=(6, 3)),
                                Pieces(piece="Pawn" ,  color="w", initial_position=(1, 4)),  Pieces(piece="Pawn" ,   color="b", initial_position=(6, 4)),
                                Pieces(piece="Pawn" ,  color="w", initial_position=(1, 5)),  Pieces(piece="Pawn" ,   color="b", initial_position=(6, 5)),
                                Pieces(piece="Pawn" ,  color="w", initial_position=(1, 6)),  Pieces(piece="Pawn" ,   color="b", initial_position=(6, 6)),
                                Pieces(piece="Pawn" ,  color="w", initial_position=(1, 7)),  Pieces(piece="Pawn" ,   color="b", initial_position=(6, 7)),]
            ### Lista de istas de 8x8
            self.__grid__ = ([[Cell(True, None) for _ in range(8)] for _ in range (8)])
            self.set_piece_cell_begining()
    

    ### Impresion del board y con las piezas en posicion actual
    def print_board(self):
        print(" --------------------------------------------------------")
        print('   {:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|'.format("", "A", "B" , "C", "D" , "E" , "F" , "G" ,"H" ))
        print(" --------------------------------------------------------")
        for i in range(8):
            row = []
            row.append(i)
            for x in range(8):
                if self.__grid__[i][x].__state__ == False:
                    row.append(str(self.__grid__[i][x].__piece__.__image__))
                else:
                    row += ' '
            print('   {:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|'.format(*row))
            print(" --------------------------------------------------------")

                

    ### Order by pieces, check the piece position, asign the 
    ### piece to the cell that belongs to the position on the grid
    def set_piece_cell_begining(self):
        for i in self.__pieces__:
            position = i.__position__
            x = position[0]
            y = position[1]
            self.__grid__[x][y].__state__ = False
            self.__grid__[x][y].__piece__ = i

